from dotenv import load_dotenv
import os
import time
import threading
# Imports the Google Cloud client library
from google.cloud import storage

load_dotenv()  # take environment variables from .env

# Instantiates a client
#storage_client = storage.Client()

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

start_time = time.time()
time_prefix = str(int(time.time()))
dummy_files = ["dummyfile1.bin", "dummyfile2.bin", "dummyfile3.bin"]

threads = list()

for file in dummy_files:

    print("uploading " + file)
    #upload_blob(os.environ.get('BUCKET_NAME'), file, time_prefix+'/'+file)
    x = threading.Thread(target=upload_blob, args=(os.environ.get('BUCKET_NAME'), file, time_prefix+'/'+file))
    threads.append(x)
    #x.start()
    #x.join()

# start threads
for x in threads:

    x.start()

# join threads
for x in threads:

    x.join()


execution_time = (time.time() - start_time)
print('Execution time in seconds: ' + str(execution_time))