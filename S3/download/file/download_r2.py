import boto3
import botocore

abs_s3_path = 'sample/sample.csv'
abs_local_location = '/home/ubuntu/sample.csv'


BUCKET_NAME = 'sample-bucket'  # replace with your bucket name
KEY = abs_s3_path  # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, abs_local_location)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
