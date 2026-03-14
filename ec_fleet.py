import boto3

ec2 = boto3.client("ec2", region_name="eu-north-1")

response = ec2.create_fleet(
    LaunchTemplateConfigs=[
        {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "practice_fleets",
                "Version": "$Latest"
            },
            "Overrides": [
                {
                    "InstanceType": "t3.micro"
                }
            ]
        }
    ],
    TargetCapacitySpecification={
        "TotalTargetCapacity": 1,
        "DefaultTargetCapacityType": "on-demand"
    },
    Type="instant"
)

print("Fleet created")
print(response["FleetId"])
