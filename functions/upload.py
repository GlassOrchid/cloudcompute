'''
References:
# https://cloud.google.com/docs/authentication/client-libraries
# https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
# https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment
'''

from google.cloud import storage
from project_secrets import BUCKET_NAME, PROJECT_ID, DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, SERVER_IP, SSH_PORT, SSH_USERNAME, SSH_PKEY, REMOTE_PORT, LOCAL_PORT


def upload_file(file, filename):
    return upload_blob(BUCKET_NAME, file, filename)

def authenticate_implicit_with_adc(project_id=PROJECT_ID):
    return storage.Client(project=project_id)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads given file to Google Cloud bucket"""
    # bucket_name = "your-bucket-name-id"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name-id"

    # NOTE: blob = binary large object

    storage_client = authenticate_implicit_with_adc()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # 0 means succeeds if there are no live versions of the blob
    generation_match_precondition = 0

    blob.upload_from_file(source_file_name, if_generation_match=generation_match_precondition)

    return f"File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}."



from sshtunnel import SSHTunnelForwarder
import os

import psycopg2
def upload_metadata(metadata):
    # SSH server details
    server_ip = SERVER_IP
    ssh_port = SSH_PORT
    ssh_username = SSH_USERNAME
    ssh_pkey = SSH_PKEY

    remote_port= REMOTE_PORT
    local_port= LOCAL_PORT

    with SSHTunnelForwarder(
        (server_ip, ssh_port),  # SSH host and port
        ssh_username=ssh_username,
        ssh_pkey=ssh_pkey,
        remote_bind_address=('127.0.0.1', remote_port),  # Address on the VM to forward to
        local_bind_address=('127.0.0.1', local_port)  # Address on your local machine
        ) as server:
            print(f"SSH tunnel established. Local port: {server.local_bind_port}")
            
            try:
                # Connect to PostgreSQL
                conn = psycopg2.connect(
                    host=DB_HOST,
                    port=DB_PORT,
                    dbname=DB_NAME,
                    user=DB_USER,
                    password=DB_PASS
                )
                # Create a cursor and execute a query
                name = metadata['filename']
                size = metadata['size']
                query = """
                    INSERT INTO files (name, size, created, modified, location)
                    VALUES (%s, %s, NOW(), NOW(), %s)
                    RETURNING id;
                """
                params = (name, size, f'/{name}')

                cur = conn.cursor()
                cur.execute(query, params)

                result = cur.fetchone()[0]  # fetchone() returns a tuple

                conn.commit()
                cur.close()
                conn.close()
                print(f"DB connection works! Result: {result}")
                return f"DB connection works! Result: {result}"
            except Exception as e:
                print(f"Connection failed: {e}", 500)
