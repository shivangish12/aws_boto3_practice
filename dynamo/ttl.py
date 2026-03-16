import boto3

def enable_ttl(table_name, ttl_attribute_name):
    """
    Enables TTL on DynamoDB table for a given attribute name
    """

    try:
        dynamodb = boto3.client("dynamodb")

        response = dynamodb.update_time_to_live(
            TableName=table_name,
            TimeToLiveSpecification={
                "Enabled": True,
                "AttributeName": ttl_attribute_name
            }
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print("TTL has been enabled successfully.")
        else:
            print("Failed to enable TTL")

    except Exception as ex:
        print(f"Couldn't enable TTL in table {table_name}. Error: {ex}")
        raise


enable_ttl("Users", "expirationDate")