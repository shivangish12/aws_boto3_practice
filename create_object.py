import boto3
from botocore.exceptions import ClientError

BUCKET_NAME="shivangi-practice-v1"
LOCAL_FILE="sample.txt"
S3_KEY="sample.txt"
s3=boto3.client("s3")

try:
    s3.upload_file(LOCAL_FILE,BUCKET_NAME,S3_KEY)
    print("Object created successfully")

except ClientError as e:
    print("Error uploading file",e)
    
