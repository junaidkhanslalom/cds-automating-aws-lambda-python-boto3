import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE= os.environ['INSTANCE_TYPE']
KEY_NAME= os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
        
    )
    
    print("New Instance created:", instance[0].id)