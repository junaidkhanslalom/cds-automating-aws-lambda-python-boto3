# Name: Deregister OLD AMis
# Environ: Python 3.7

# Summary: Create lambda, iterate over region, ami, looking for it older 2 days, grant roll, for cloudwatch and register and deregistering 
import datetime
from dateutil.parser import parse

import boto3

def days_old(date):
    parsed = parse(date).replace(tzinfo=None)
    diff = datetime.datetime.now() - parsed
    return diff.days

def lambda_handler(event, context):

    # GEt list of all region
    ec2_client = boto3.client('ec2')
    regions = [region['RegionsName']
            for region in ec2_client.describe_regions()['Regions']]


    for region in regions:
        ec2 = boto3.client('ec2', region_name=region)
        print("Region:", region)


        amis = ec2.describe_images(Owner=['self'])['Images']

        for ami in amis:
           creation_date = ami['CreationDate']
           age_days = days_old(creation_date)
           image_id=ami['ImageId']
           print('ImageId: {}, CreationDate: {} ({} days old)'.format(image_id, creation_date, age_days)) 

           if age_days >=2:
               print("Delete ImageId:", image_id)

               # Deregister the AMI
               ec2.deregister_image(ImageId=image_id)



# Increase time out across regions 
# Scheduled: daily basis, create a rule and run on a schedule, add target (lambda functions)

