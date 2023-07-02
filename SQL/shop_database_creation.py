import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)
my_cursor = mydb.cursor()
sql = "create database shop"
my_cursor.execute(sql)
print("Database created successfully")
