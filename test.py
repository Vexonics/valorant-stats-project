import requests
import os

api_key = os.getenv("HDEV-6474ec4a-fd19-45b5-9982-8395909e6a55")  
headers = {
    "Authorization": f"Bearer {api_key}"
}

url = "https://api.henrikdev.xyz/valorant/v4/status/na"  # free endpoint

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.text)