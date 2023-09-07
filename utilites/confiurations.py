import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\Abhishek.sharma\\PycharmProjects\\pythonProject4august\\utilites\\properties.ini')
    return config

connect_config ={
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database']
}

def getPassword():
    return "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"

def getConnection():
    try :
        connection = mysql.connector.connect(**connect_config)
        if connection.is_connected():
            print("connection Succesful")
            return connection
    except Error as e:
        print(e)

    # connection = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='root')
    #
    # return connection

def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    row2 = cursor.fetchone()
    conn.close()

    return row2

