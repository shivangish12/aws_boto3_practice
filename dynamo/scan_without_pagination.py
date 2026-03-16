import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

response = table.scan()

items = response["Items"]

print("Number of items returned:", len(items))