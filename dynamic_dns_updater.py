# Updates route53 dns records to reflect current IP
# should be run from CRON to update on recurring basis
# based on this excellent guide:
# https://willwarren.com/2014/07/03/roll-dynamic-dns-service-using-amazon-route53/
import os
import pprint

import boto3
import requests
import yaml

determine_ip_url = 'http://icanhazip.com'
ip_resp = requests.get(determine_ip_url)
ip = ip_resp.text.strip()

# Load user/domain specific config from file
config_file = open('config.yaml')
config = yaml.load(config_file)
hosted_zone_id = config['hosted_zone_id']
record_set_name = config['record_set_name']
ttl = int(config['ttl'])

old_ip = None
old_ip_file_path = 'old_ip'
if os.path.exists(old_ip_file_path):
    old_ip = open(old_ip_file_path).read().strip()

if ip == old_ip:
    print('ip not changed')
    exit(0)

client = boto3.client('route53')
response = client.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch={
        'Comment': 'Dynamic DNS Update',
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': record_set_name,
                    'Type': 'A',
                    'TTL': ttl,
                    'ResourceRecords': [
                        {
                            'Value': ip
                        },
                    ],
                }
            },
        ]
    }
)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(response)

status_code = response['ResponseMetadata']['HTTPStatusCode']
if status_code == 200:
    old_ip_file = open(old_ip_file_path, 'w')
    old_ip_file.write(ip)
    old_ip_file.close()
