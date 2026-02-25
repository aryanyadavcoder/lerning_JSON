import requests
import json

response = requests.get("https://aryanyadavcoder.github.io/lerning_JSON/result1.json")
data=[{"name":"amit","rollno":45,"math":65,"englih":56},{"name":"rohit","rollno":40,"math":55,"englih":46}]
data =str( response.json())
# data=json.loads(data)
print(data)
# for key,value in data.items():
#     print(key,value)

print(data)