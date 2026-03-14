import boto3

ec2 = boto3.client("ec2", region_name="eu-north-1")

response = ec2.delete_fleets(
    FleetIds=["fleet-11951ca5-6d84-4e9c-0eb2-0728d4fee8a9"],
    TerminateInstances=True
)

print(response)
