import requests
import json


response = requests.get("https://raw.githubusercontent.com/aryanyadavcoder/lerning_JSON/refs/heads/main/class2.json")
data = response.json()
print(data)


 

response = requests.get("https://raw.githubusercontent.com/aryanyadavcoder/lerning_JSON/refs/heads/main/class1.json")
data = response.json()
print(data)
