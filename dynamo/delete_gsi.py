import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.update_table(
    TableName='Users',
    GlobalSecondaryIndexUpdates=[
        {
            'Delete': {
                'IndexName': 'CountryIndex'
            }
        }
    ]
)

print(response)