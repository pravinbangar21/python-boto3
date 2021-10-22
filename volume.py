# import boto3
# AWS_REGION="us-east-2"
 
# ec2_client=boto3.client("ec2",region_name=AWS_REGION)
 
# new_volume=ec2_client.create_volume(
#     AvailabilityZone=f'{AWS_REGION}c',
#     Size=10,
#     VolumeType='gp2',
#     TagSpecifications=[
#         {
#             'ResourceType': 'volume',
#             'Tags': [
#                 {
#                     'Key': 'Name',
#                     'Value': 'pravin-volume'
#                 }
#             ]
#         }
#     ]
# )
 
# print(f"Created volume ID: {new_volume['VolumeId']}")


import boto3
AWS_REGION="us-east-2"
 
ec2_resource=boto3.resource("ec2",region_name=AWS_REGION)
 
volumeCollection=ec2_resource.volumes.all()
 
for volume in volumeCollection:
    print(volume)

