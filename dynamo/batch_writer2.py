import boto3

dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("Users")

with table.batch_writer() as writer:
    for i in range(100):
        writer.put_item(
            Item={
                "user_id": f"user#{i}",
                "name": f"user{i}",
                "age": i
            }
        )