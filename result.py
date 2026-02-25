import requests
import json

response = requests.get("https://raw.githubusercontent.com/aryanyadavcoder/lerning_JSON/refs/heads/main/result1.json")
data =str( response.json())
# data=json.loads(data)
print(data)
# for key,value in data.items():
#     print(key,value)