import boto3

client = boto3.client("dynamodb")

client.create_table(
    TableName="Users",
    KeySchema=[
        {"AttributeName": "user_id", "KeyType": "HASH"}
    ],
    AttributeDefinitions=[
        {"AttributeName": "user_id", "AttributeType": "S"}
    ],
    BillingMode="PAY_PER_REQUEST"
)



