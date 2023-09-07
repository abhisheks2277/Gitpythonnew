import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty'},)
# print(response.text)
# print(type(response.text))

json_response = response.json()

for actualbook in json_response:
    if actualbook['isbn']  == 'RGHCC':
        print(actualbook)