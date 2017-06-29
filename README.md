# Dynamic DNS Updater

This is a little utility that can be used to dynamically updated a DNS 'A' record
on Route53, in order to maintain the availability of a home server with a dynamic IP address.
It is intended to be run with cron.

## Setup

If you have not previously set up the AWS CLI on your machine, follow the [install instructions](http://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux.html).
Once you have the AWS CLI working, proceed to run the following commands:

```
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Then create YAML config file named `config.yaml` containing the following fields:

```
hosted_zone_id: ${YOUR_HOSTED_ZONE_ID}
record_set_name: ${YOUR_RECORD_SET_NAME}
ttl: ${YOUR_TTL}
```
