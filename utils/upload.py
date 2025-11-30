'''
References:
# https://cloud.google.com/docs/authentication/client-libraries
# https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
# https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment
'''

from google.cloud import storage
from project_secrets import BUCKET_NAME
from flask import flash
import tempfile
from pathlib import Path
import os
from .authenticate import authenticate_implicit_with_adc, connect_postgres
from .queries import INSERT_FILE_QUERY


def handle_upload(file, filename, args):
    """Handles uploading the file and metadata if enabled."""
    from .file import get_file_metadata

    # Save file temporarily for metadata
    with tempfile.NamedTemporaryFile(delete_on_close=True) as tmp:
        file.save(tmp)
        tmp_path = Path(tmp.name)

        tmp.flush()
        os.fsync(tmp.fileno())

        metadata = get_file_metadata(tmp_path, filename)
        print(metadata)

        if args.metadata:
            upload_metadata(metadata)  
    
        if args.online:
            result = upload_blob(BUCKET_NAME, file, filename)
            flash(result)
        else:
            flash("Application is currently not uploading files.") 

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

    try:
        blob.upload_from_file(source_file_name, if_generation_match=generation_match_precondition, rewind=True)
        return f"File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}."
    except Exception as e:
        print(f"Upload failed: {e}", 500)

def upload_metadata(metadata):
    conn = connect_postgres()
    try:
        with conn.cursor() as cur:
            # Create a cursor and execute a query
            name = metadata['filename']
            file_type = metadata['filetype']
            size = metadata['size']
            created = metadata['created']
            modified = metadata['modified']

            params = [name, file_type, size, created, modified, f'/{name}']

            cur.execute(INSERT_FILE_QUERY, params)
            result = cur.fetchone()[0]  # fetchone() returns a tuple
            conn.commit()
            return f"DB entry created with ID: {result}"
    except Exception as e:
        print(f"Upload Connection failed: {e}", 500)
    finally:
        conn.commit()
        conn.close()