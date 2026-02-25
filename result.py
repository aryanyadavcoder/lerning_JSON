import requests
import json

response = requests.get("https://aryanyadavcoder.github.io/lerning_JSON/result1.json")
data =str( response.json())
data=json.loads(data)
print(data)
# for key,value in data.items():
#     print(key,value)