
import boto3
# cw=boto3.client("cloudwatch")
 
# response=cw.delete_alarms(
#     AlarmNames=["pravin_webserver_cpuutilization"]
# )
 
# print(response)

class DesDemo:
    def __init__(self):
        print("Welcome")
    def __del__(self):   #destructor
        print("Bye")
 
print("1st")
dd=DesDemo()
del dd   #destructor  ..free memory/space
print("2nd")