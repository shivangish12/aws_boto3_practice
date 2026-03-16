import boto3

client = boto3.client("dynamodb")

client.update_table(
    TableName="Users",
    AttributeDefinitions=[
        {"AttributeName": "country", "AttributeType": "S"}
    ],
    GlobalSecondaryIndexUpdates=[
        {
            "Create": {
                "IndexName": "CountryIndex",
                "KeySchema": [
                    {"AttributeName": "country", "KeyType": "HASH"}
                ],
                "Projection": {
                    "ProjectionType": "ALL"
                }
            }
        }
    ]
)