import requests
import json

response=requests.get('https://jsonplaceholder.typicode.com/users/1/todos/')

response_json=json.loads(response.text)

print(response_json[0])
print()

for todo in response_json:
    if todo['id']==5:
        print(todo['title'])