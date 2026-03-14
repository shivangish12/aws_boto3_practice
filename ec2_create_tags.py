import boto3

ec2 = boto3.client(
    'ec2',
    region_name='eu-north-1'
)

instance_id = "i-0d2562ae18985b254"
ec2.create_tags(
    Resources=['i-0d2562ae18985b254'],
    Tags=[
        {'Key': 'Environment', 'Value': 'Practice'},
        {'Key': 'Owner', 'Value': 'Shivangi'}
    ]
)

print("Tags added successfully")