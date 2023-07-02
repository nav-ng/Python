# create database school
# create table students
# it has id, student name,school name,roll no,department,mark


import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()
sql = "create database school"
mycursor.execute(sql)
print("database created successfully")
