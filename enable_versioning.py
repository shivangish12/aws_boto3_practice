import boto3

s3=boto3.client("s3")
bucket_name="shivangi-practice-aws-boto3-demo"
s3.put_bucket_versioning(Bucket=bucket_name, VersioningConfiguration={"Status":"Enabled"})
print("Versioning successful")