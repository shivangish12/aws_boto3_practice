import boto3

client = boto3.client("dynamodb")

response = client.execute_statement(
    Statement="SELECT * FROM Users WHERE attribute_exists(expirationDate)"
)

print(response["Items"])