import boto3

ec2=boto3.client("ec2")

res=ec2.create_key_pair(
    KeyName="p3cvv1"
)
#response=ec2.describe_key_pairs()

#print(response)
print(res)

#with open("pravin-key.pem","w") as f:  #file pointer
#    f.write(res["KeyMaterial"])

f=open("pravin-key.pem","w")
f.write(res["KeyMaterial"])