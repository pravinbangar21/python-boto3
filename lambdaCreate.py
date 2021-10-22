import boto3

iam_client=boto3.client("iam")

lambda_client=boto3.client("lambda")
print("Client is ready")
zipped_code=None

with open("lambda.zip","rb") as f:
    zipped_code=f.read()

    iam_role=iam_client.get_role(RoleName="rl_serverless_mujahed")
    print("Role is createdd")
    res=lambda_client.create_function(

        FunctionName="FunPravin",
        Runtime="python3.9",
        Role=iam_role["Role"]["Arn"],
        Handler="handler.lambda_handler",
        Code=dict(ZipFile=zipped_code),
        TimeOut=300
    )
    print("-------------------")
    print(res)



