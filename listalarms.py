import boto3
cloudwatch=boto3.client("cloudwatch")

paginator=cloudwatch.get_paginator("describe_alarms")

for page in paginator.paginate(StateValue="INSUFFICIENT_DATA"):
    print(page["MetricAlarms"])
