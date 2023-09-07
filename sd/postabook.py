import requests
import configparser
from payload import *
from utilites.confiurations import *
from utilites.resources import *

# url_addbook = getConfig()['API']['endpoint']+ApiResources.addBook
# url_deletebook = getConfig()['API']['endpoint']+ApiResources.deleteBook
# headers = {"Content-Type":"application/json"}
# addBook_response = requests.post(url_addbook,json=addBookPayload("fefressdswse"),headers=headers,)
#
# print(addBook_response.json())\
#
#
# print(type(addBook_response.json()))
# response_json = addBook_response.json()
# bookid = response_json['ID']
#
#
# ######delete the book########
#
# response_delete = requests.post(url_deletebook,json={
#     "ID":bookid
# },headers= headers)
#
# assert  response_delete.status_code ==200
# res_json = response_delete.json()
#
# print(res_json['msg'])

#authentication
se = requests.session()
se.auth = auth=('abhisheks2277',getPassword())

url ='https://api.github.com/user'
# url ="https://github.com/abhisheks2277"
github_response = requests.get(url,verify=False,auth=('abhisheks2277',getPassword()))

print(github_response.status_code)
# print(github_response.text)


url2 ='https://api.github.com/user/repos'

response = se.get(url2)
print(response.status_code)

