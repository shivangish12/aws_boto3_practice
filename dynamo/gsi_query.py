import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")
response = table.query(
    IndexName="CountryIndex",
    KeyConditionExpression=Key("country").eq("India")
)

print(response["Items"])