# it is a function used in mysql to return the minimum value from a mysql table
# it is used to return the maximum value

import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
sql = "select min(mark) as smallestmark from student"
mycursor.execute(sql)
a = mycursor.fetchone()
b=a[0]
print("Smallest mark is", b)
