
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


# ===========================



# import boto3
 
# AWS_REGION="ap-south-1"
# ec2=boto3.client("ec2",region_name=AWS_REGION)

import boto3

#ec2=boto3.resource("ec2")
ec2=boto3.resource('ec2',region_name="ap-southeast-1")

# response=ec2.create_instances(
#     ImageId="ami-0d058fe428540cd89",MinCount=1,MaxCount=2)

instances=ec2.instances.filter(
    Filters=[{"Name":"instance-state-name","values":["running"]}]
)
for myserver in instances:
    print(myserver.id,myserver.instance_type)
    # print(response) 
#     ,
#     TagSpecifications=[
#         {
#             "ResourceType":"ec2",
#             "Tags":[
#                 {
#                     "Key":"Name",
#                     "Value":"pravinvec2me"
#                 }
#             ]
#         }
#     ]
# )






# import boto3
# ec2=boto3.client("ec2")

# response=ec2.describe_regions()
# print(response["Regions"])

# response=ec2.describe_availability_zones()
# print(response["AvailabilityZones"])


# newVolume=ec2.create_volume(
#     AvailabilityZone=f"{AWS_REGION}c",
#     Size=11,
#     VolumeType="gp2",
#     TagSpecifications=[
#         {
#             "ResourceType":"volume",
#             "Tags":[
#                 {
#                     "Key":"Name",
#                     "Value":"pravinvolume"
#                 }
#             ]
#         }
#     ]
# )
 
# print(f'Created Volume with ID: {newVolume["VolumeId"]}')

