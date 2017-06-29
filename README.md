# Dynamic DNS Updater

This is a little utility that can be used to dynamically updated a DNS 'A' record
on Route53, in order to maintain the availability of a home server with a dynamic IP address.
It is intended to be run with cron.

## Setup

Run the following commands:

```
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```
