import boto3

s3 = boto3.client("s3")

etag = '"4df85009e61545ff4b05ca969602989a"'  # include quotes

with open("sample.txt", "w") as f:
    f.write("Version 2")

s3.put_object(
    Bucket="shivangi-practice-v1",
    Key="sample.txt",
    Body=open("sample.txt", "rb"),
    IfMatch=etag
)

print("Upload successful")
