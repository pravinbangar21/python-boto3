import boto3

cw_client=boto3.client("cloudwatch")

response=cw_client.put_metric_alarm(
    AlarmName="pravin_webserver_cpuutilization",
    ComparisonOperator="GreaterThanThreshold",
    EvaluationPeriods=1,
    MetricName="CPUUtilization",
    Namespace="AWS/EC2",
    Period=60,
    Statistic="Average",
    Threshold=70.0,
    ActionsEnabled=False,
    AlarmDescription="This is Web Server Alarm for CPU Utilization",
    Dimensions=[
        {
            "Name":"InstanceId",
            "Value":"INSTANCE_ID"
        }
    ],
    Unit="Seconds"
)
print(response)