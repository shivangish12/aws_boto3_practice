import boto3

s3 = boto3.client("s3")

response = s3.head_object(
    Bucket="shivangi-practice-v1",
    Key="sample.txt"
)

print("ETag:", response["ETag"])
print("LastModified:", response["LastModified"])
