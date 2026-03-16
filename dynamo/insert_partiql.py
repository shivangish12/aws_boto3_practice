import boto3

client=boto3.client("dynamodb")
response = client.execute_statement(
    Statement="INSERT INTO Users VALUE {'user_id':'4', 'name':'Rahul'}"
)