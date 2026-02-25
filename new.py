import requests
import json


response = requests.get("https://raw.githubusercontent.com/aryanyadavcoder/lerning_JSON/refs/heads/main/data.json")
data = response.json()
print(data)


 

response = requests.get("https://raw.githubusercontent.com/aryanyadavcoder/lerning_JSON/refs/heads/main/data1.json")
data = response.json()
print(data)
