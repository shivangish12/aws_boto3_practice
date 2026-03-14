import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("Users")

table.put_item(
    Item={
        "user_id": "2",
        "name": "S",
        "age": 28
    }
)