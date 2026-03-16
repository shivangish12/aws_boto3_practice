import boto3

dynamodb = boto3.client("dynamodb")

table_name = "Users"
index_name = "CountryIndex"

response = dynamodb.describe_table(TableName=table_name)

indexes = response["Table"].get("GlobalSecondaryIndexes", [])

index_exists = any(idx["IndexName"] == index_name for idx in indexes)

if index_exists:
    print("GSI still exists")
else:
    print("GSI has been removed")