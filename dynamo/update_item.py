import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

response = table.update_item(
    Key={
        "user_id": "1"
    },
    UpdateExpression="SET #n = :name",
    ExpressionAttributeNames={
        "#n": "name"
    },
    ExpressionAttributeValues={
        ":name": "Shivangi"
    },
    ReturnValues="UPDATED_NEW"
)

print(response)