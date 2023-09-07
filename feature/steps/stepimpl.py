import sys
sys.path.append('C:\\Users\\Abhishek.sharma\\PycharmProjects\\pythonProject4august\\')
# Adjust the path accordingly
from behave import *
import requests
from utilites.resources import *
from utilites.confiurations import *
from utilites.payload import *


@given('the Book details WHich needs to be added to Library')
def step_impl(context):
    context.url_addbook = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("masnfzssdsaxdss",'423')


@when('we execute the Addbook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url_addbook, json=context.payLoad, headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookid = response_json['ID']
    print(context.bookid)
    assert response_json['Msg'] == 'successfully added'


@given('the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url_addbook = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload(isbn,aisle)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('abhisheks2277', getPassword())


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then('status code of response should be {statusCode:d}')
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
