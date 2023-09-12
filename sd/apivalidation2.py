import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty'},)
# print(response.text)
# print(type(response.text))

json_response = response.json()
print(json_response)
print(json_response)
print(json_response)


print(json_response)
print(json_response)
print(json_response)
print(type(response.text))
print(type(response.text))

for actualbook in json_response:
    if actualbook['isbn']  == 'RGHCC':
        print(actualbook)