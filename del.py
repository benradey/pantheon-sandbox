import requests
url = "https://pantheon.corp.qa.redhat.com/content/repositories/pantheon-v2-test-repo"

payload = {":operation": "delete"}

response = requests.post(url, data=payload, auth=("sync-service","sync-service"))

print(response.text)
print(response.status_code)
