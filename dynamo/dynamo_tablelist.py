import boto3

dynamodb = boto3.client("dynamodb")

table_name = "Users"

try:
    response = dynamodb.describe_table(TableName=table_name)
    print("Table exists")
except dynamodb.exceptions.ResourceNotFoundException:
    print("Table does not exist")