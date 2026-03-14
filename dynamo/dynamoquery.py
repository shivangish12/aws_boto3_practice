import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

response = table.query(
    KeyConditionExpression=Key("user_id").eq("1")
)

for item in response["Items"]:
    print(item["name"])