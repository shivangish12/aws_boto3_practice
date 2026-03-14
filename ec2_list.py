import boto3

ec2 = boto3.client(
    'ec2',
    region_name='eu-north-1'
)

instance_id = "i-0d2562ae18985b254"

response = ec2.describe_instances(
    InstanceIds=[instance_id]
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])
        print("State:", instance['State']['Name'])
        print("AZ:", instance['Placement']['AvailabilityZone'])
        print("Private IP:", instance['PrivateIpAddress'])
