import mysql.connector
from utilites.confiurations import *
# host, database, authentication(user,password)
connection = getConnection()

# print(connection.is_connected())

cursor = connection.cursor()
cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()
# print(row)
# print(row[3])
rowall =cursor.fetchall()
print(rowall)


print(rowall[2][3])
ad =0
for row in rowall:
    ad+= row[2]

print(ad)

query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK","Jmeter")

cursor.execute(query,data)
connection.commit()

print(rowall)

connection.close()