import boto3

s3=boto3.client("s3",region_name="ap-south-1")
bucket_name="shivangi-practice-aws-boto3-demo"
response=s3.create_bucket(Bucket=bucket_name,
                          CreateBucketConfiguration={
                              "LocationConstraint":"ap-south-1"
                          })
print("Bucket created:", bucket_name)