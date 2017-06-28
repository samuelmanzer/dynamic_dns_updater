import requests

determine_ip_url = 'http://icanhazip.com'
ip_resp = requests.get(determine_ip_url)
ip = ip_resp.text.strip()
print(ip)
