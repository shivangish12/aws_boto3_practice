import boto3

s3 = boto3.client("s3", region_name="eu-north-1")

bucket_name = "shivangi-practice-v1"
object_key = "presignedurl.txt"

url = s3.generate_presigned_url(
    ClientMethod="put_object",
    Params={
        "Bucket": bucket_name,
        "Key": object_key,
        "ContentType": "text/plain"
    },
    ExpiresIn=300  # 5 minutes
)

print("Presigned URL:")
print(url)
