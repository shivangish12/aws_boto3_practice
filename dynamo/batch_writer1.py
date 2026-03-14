import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

with table.batch_writer() as batch:
    batch.put_item(
        Item={"user_id": "1", "name": "Amit", "age": 25}
    )
    batch.put_item(
        Item={"user_id": "2", "name": "Rahul", "age": 28}
    )
    batch.put_item(
        Item={"user_id": "3", "name": "Priya", "age": 24}
    )