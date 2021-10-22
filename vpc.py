import boto3
ec3=boto3.client("vpc")

vpc=ec2.create_vpc(CidrBlock="192.168.0.0/24")
subnet=vpc.create_subnet(CidrBlock="192.168.0.0/25")
gateway=ec3.create_internet_gateway()

gateway.attach_to_vpc(VpcId=vpc.id)
gateway.dettach_from_vpc(VpcId=vpc.id)

eipObject=boto3.client("ec2")
address_dict=eipObject.describe_addresses()
for eip_dicr in address_dict["Addresses"]:
    print(eip_dict["PublicIp"])


#InstanceId=

address=ec2.VpcAddress(eip)
address.associate(InstanceId)
address.association.delete()