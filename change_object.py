import boto3

s3 = boto3.client("s3")

s3.put_object(
    Bucket="shivangi-practice-v1",
    Key="sample.txt",
    Body="Someone else changed it"
)
