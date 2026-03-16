import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

table.put_item(
    Item={
        "user_id": "u1",
        "name": "Shivangi",
        "country": "India",
        "created_at": "2026-03-16"
    }
)

table.put_item(
    Item={
        "user_id": "u2",
        "name": "Rahul",
        "country": "India",
        "created_at": "2026-03-15"
    }
)