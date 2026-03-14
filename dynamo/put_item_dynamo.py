import boto3

client=boto3.client("dynamodb")
client.put_item(
    TableName="Users",
    Item={
        "user_id": {"S": "1"},
        "name": {"S": "Shivangi"},
        "age": {"N": "30"}
    }
)