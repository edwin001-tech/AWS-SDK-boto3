# This Python program prints the availability zones available
# Import AWS Python boto3 library.
import boto3
# Create an object
target = boto3.client('ec2')
# Retrieves the Availability Zones for the current Region
response = target.describe_availability_zones()
# Loop over data structure
for n in range(len(response['AvailabilityZones'])):
 az_name = response['AvailabilityZones'][n]['ZoneName']
 az_id = response['AvailabilityZones'][n]['ZoneId']
 state = response['AvailabilityZones'][n]['State']
print(n+1,')','The availability zone', az_name, 'with ID', az_id, 'is', state)