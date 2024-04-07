import requests
import json

response=requests.get('https://jsonplaceholder.typicode.com/users/1/')

response_json=json.loads(response.text)

print(response_json)
print()

street=response_json['address']

print(street)

print()
data_serialized=json.dump(street, open('address.json',"w"),indent=4)
