# -*- coding: utf-8 -*-

from boto3.session import Session

profile = 'sample-profile'
session = Session(profile_name=profile)

# Create an S3 client
s3 = session.client('s3')

# Call S3 to list current buckets
response = s3.list_objects(
    Bucket='sample-bucket',
    Prefix=''
)


if 'Contents' in response:
    keys = [content['Key'] for content in response['Contents']]

for key in keys:
    print(key)
