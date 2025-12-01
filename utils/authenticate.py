from google.cloud import storage
from sshtunnel import SSHTunnelForwarder
from project_secrets import (
    PROJECT_ID,
    DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER,
    SERVER_IP, SSH_PORT, SSH_USERNAME, SSH_PKEY,
    REMOTE_PORT, LOCAL_PORT
)
import psycopg2

# Authenticate with Google Cloud using Application Default Credentials
def authenticate_implicit_with_adc(project_id=PROJECT_ID):
    return storage.Client(project=project_id)         

# Create and return an SSH tunnel for secure database access
def create_ssh_tunnel():
    return SSHTunnelForwarder(
        (SERVER_IP, SSH_PORT),
        ssh_username=SSH_USERNAME,
        ssh_pkey=SSH_PKEY,
        remote_bind_address=('127.0.0.1', REMOTE_PORT),
        local_bind_address=('0.0.0.0', LOCAL_PORT)
    )

# Establish a connection to the PostgreSQL database
def connect_postgres():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except Exception as e:
        print(f"Database Connection failed: {e}", 500)
