import boto3
import time

client = boto3.client("dynamodb")

expiration_time = int(time.time()) + 3600  # 1 hour from now

client.update_item(
    TableName="Users",
    Key={
        "user_id": {"S": "1"}   # your partition key
    },
    UpdateExpression="SET expirationDate = :ttl",
    ExpressionAttributeValues={
        ":ttl": {"N": str(expiration_time)}
    }
)

print("Item updated with expirationDate")