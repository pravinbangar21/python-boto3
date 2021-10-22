import boto3

client=boto3.client("rds")

response=client.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    DBInstanceIdentifier="pravin-db-02",
    Engine="MySQL",
    MasterUsername="pravin1",
    MasterUserPassword="testrdsss2129"

)

print(response)

# DB RDS instance
# check public access - SG group ID
#ENd point check

# mysql -h rds-endpoint -u admin1 -p password


# response=client.describe_db_instances(
#     DBInstanceIdentifier="",
#     Filters=[
#         {
#             "Name":"engine",
#             "Values":["MySQL"]
#         }
#     ]
# )
 
# print(response)


# import boto3
 
# client=boto3.client("rds")
 
# response = client.stop_db_instance(
#     DBInstanceIdentifier='mujahed-db-instance-01',
#     DBSnapshotIdentifier='stop-snapshot001'
# )
 

# response = client.start_db_instance(
#     DBInstanceIdentifier='mujahed-db-instance-01'
# )
 
# response = client.modify_db_instance(
#     DBInstanceIdentifier='mujahed-db-instance-01',
#     MasterUserPassword="NEW PASSWORD"
# )
 

# response = client.create_db_instance_read_replica(
#     DBInstanceIdentifier='mujahed-db-instance-01',
#     PublicyAccessible=True,
#     DBInstanceClass="db.t2.micro",
#     SourceDBInstanceIdentifier="mujahed-db-instance-01-read-replica",
#     StorageType="gp2",
#     Tags=[
#         {
#             "Key":"ReadreplicaNumber",
#             "Value":"readreplica001"
#         }
#     ]
# )