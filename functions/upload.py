'''
References:
# https://cloud.google.com/docs/authentication/client-libraries
# https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
# https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment
'''

from google.cloud import storage
import project_secrets as ps


def upload_file(file, filename):
    return upload_blob(ps.BUCKET_NAME, file, filename)

def authenticate_implicit_with_adc(project_id=ps.PROJECT_ID):
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


