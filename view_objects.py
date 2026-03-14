import boto3

s3=boto3.client("s3")
response=s3.list_objects_v2(Bucket="shivangi-practice-v1")
print(response["Contents"])

for obj_name in response["Contents"]:
    print(obj_name["Key"])