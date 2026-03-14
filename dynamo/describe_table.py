import boto3
from botocore.exceptions import ClientError

client=boto3.client("dynamodb")
def describe_table(table_name):
   
    try:
        response = client.describe_table(TableName=table_name)
        table = response["Table"]
 
        print(f"📋 Table Description: {table['TableName']}")
        print(f"   Status      : {table['TableStatus']}")
        print(f"   ARN         : {table['TableArn']}")
        print(f"   Item Count  : {table['ItemCount']}")
        print(f"   Size (bytes): {table['TableSizeBytes']}")
 
        throughput = table["ProvisionedThroughput"]
        print(f"   RCU / WCU   : {throughput['ReadCapacityUnits']} / {throughput['WriteCapacityUnits']}")
        
 
        print(f"   Key Schema  :")
        for key in table["KeySchema"]:
            print(f"     {key['KeyType']:6s} → {key['AttributeName']}")
 
        return table
 
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            print(f"Table '{table_name}' not found. It may still be creating — retry in a few seconds.")
        else:
            print(f"Error: {e.response['Error']['Message']}")


describe_table("Users")