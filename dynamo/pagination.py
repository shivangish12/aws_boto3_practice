import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

response = table.scan()

items = response["Items"]
# 1 MB is the limit
while "LastEvaluatedKey" in response:
    
    response = table.scan(
        ExclusiveStartKey=response["LastEvaluatedKey"]
    )

    items.extend(response["Items"])

print(len(items))