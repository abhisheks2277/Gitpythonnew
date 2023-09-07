import sys
sys.path.append('C:\\Users\\Abhishek.sharma\\PycharmProjects\\pythonProject4august\\')
# Adjust the path accordingly
from behave import *
import requests
from utilites.confiurations import *
from utilites.resources import *
from utilites.payload import *


def after_scenario(context,scenario):
    if "library" in scenario.tags:
        url_deletebook = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        response_delete = requests.post(url_deletebook, json={"ID": context.bookid}, headers=context.headers)

        assert response_delete.status_code == 200
        res_json = response_delete.json()

        print(res_json['msg'])