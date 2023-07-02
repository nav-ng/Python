# what is pymysql
# it is a module that is used to connect your mysql and python.
import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()  # cursor object

# cursor object which is used to select , retrieve data from a set of rows.
# and also it is used to execute and sql command.

sql = "create database employee"
mycursor.execute(sql)
print("database created successfully")

