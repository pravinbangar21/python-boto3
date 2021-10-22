# import boto3
# ec2=boto3.client("ec2",region_name="us-west-2")
    #ap-northeast-1")
# ec2=boto3.resource("ec2",region_name="us-west-2")
# response=ec2.create_instances(
#     BlockDeviceMappings=[
#         {
#             "DeviceName":"/dev/xvda",
#             "Ebs":{
#                 "DeleteOnTermination":True,
#                 "VolumeSize":10,
#                 "VolumeType":"gp2"
#             }
#         }
#     ],
#     ImageId="ami-087107f9778206adb",
#     InstanceType="t2.micro",
#     MinCount=1,
#     MaxCount=2,
#     Monitoring={
#         "Enabled":False
#     },
#     SecurityGroupIds=[
#         "sg-abaefd32dc3d23"
#     ]
# )

import boto3
ec2=boto3.resource("ec2",region_name="us-east-1")
response=ec2.create_instances(
    BlockDeviceMappings=[
        {
            "DeviceName":"/dev/xvda",
            "Ebs":{
                "DeleteOnTermination":True,
                "VolumeSize":10,
                "VolumeType":"gp2"
            }
        }
    ],
    ImageId="ami-087107f9778206adb",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=2,
    Monitoring={
        "Enabled":False
    },
    SecurityGroupIds=[
        "sg-00246d1b233b6c199"
    ]
)

print(response[0].id)

# import boto3
# ec2=boto3.client("ec2",region_name="us-west-2")
# response=ec2.create_instances(
#     BlockDeviceMapping=[
#         {
#             "DeviceName":"/dev/xvda",
#             "Ebs":{
#                 "DeleteOnTermination":True
#                 "VolumeSize":10
#                 "VOlumeType":"gp2"
#             }
#         }
#     ],
#     ImageId="ami-087107f9778206adb",
#     instanceType="t2.micro",
#     MinCount=1,
#     MaxCount=2,
#     Monitoring={
#         "Enabled":False
#     },
#     SecurityGroupIds=[
#         "sg-abaefd32dc3d23"

#     ]
# )