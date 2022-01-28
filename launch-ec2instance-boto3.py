import boto3
response = ec2.run_instances(
    ImageID="ami-randomlettsAndnums",
    InstanceType="t2.micro",
    KeyName="ec2-key-name",
    MinCount=1,
    MaxCount=1
)