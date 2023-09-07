import requests
import configparser
from payload import *
from utilites.confiurations import *
from utilites.resources import *
from sd.payload import *

url_addbook = getConfig()['API']['endpoint']+ApiResources.addBook
url_deletebook = getConfig()['API']['endpoint']+ApiResources.deleteBook
query = 'select * from Books'
headers = {"Content-Type":"application/json"}

addBook_response = requests.post(url_addbook, json=buildPayLoadFromDB(query), headers=headers)

print(addBook_response.json())

print(type(addBook_response.json()))
response_json = addBook_response.json()
bookid = response_json['ID']

######delete the book########

response_delete = requests.delete(url_deletebook, json={"ID": bookid}, headers=headers)

# assert response_delete.status_code == 200
res_json = response_delete.json()

print(res_json['msg'])
