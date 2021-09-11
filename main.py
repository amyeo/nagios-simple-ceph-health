import requests
import json
import sys
import urllib3

urllib3.disable_warnings() #disable self signed cert warning

api_token = None
endpoint = 'https://mgrnode:8443/api/auth'
headers = {
        'Accept':'application/vnd.ceph.api.v1.0+json',
        'Content-Type':'application/json',
        }

#username and password are for example only
form_data = {
        'username':'nagios-readonly',
        'password':'123',
        }

response = requests.post(endpoint, headers=headers, data=json.dumps(form_data), verify=False)
if "token" not in response.json():
    print("No token. Check username, password and endpoint.")
    sys.exit(2) #critical

api_token = response.json()["token"]
headers["Authorization"] = f"Bearer {api_token}"

#get health
endpoint = 'https://mgrnode:8443/api/health/minimal'
response = requests.get(endpoint, headers=headers, verify=False)
cluster_status = response.json()["health"]["status"]
print(cluster_status)
if cluster_status == 'HEALTH_OK':
    sys.exit(0)
sys.exit(1) #exit w/ warning
