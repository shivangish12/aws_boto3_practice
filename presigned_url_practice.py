import boto3
from datetime import timedelta
from botocore.client import Config

s3 = boto3.client(
    "s3",
    region_name="eu-north-1",
    config=Config(signature_version="s3v4")
)

bucket_name = "shivangi-practice-v1"
object_key = "sample.txt"

url = s3.generate_presigned_url(
    ClientMethod="get_object",
    Params={
        "Bucket": bucket_name,
        "Key": object_key
    },
    ExpiresIn=300 
)

print("Presigned URL (GET):")
print(url)
