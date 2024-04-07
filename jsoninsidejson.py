import requests
import json

response=requests.get('https://jsonplaceholder.typicode.com/users/1/')

response_json=json.loads(response.text)

print(response_json)
print()

street=response_json['address']['street']

print(street)