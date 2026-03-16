import boto3

client = boto3.client("dynamodb")

response = client.execute_statement(
    Statement="SELECT * FROM Users WHERE user_id = '1'"
)

print(response['Items'])