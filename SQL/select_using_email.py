import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor = mydb.cursor()
email = input("Enter email to be searched:")
sql = "select * from person where email='%s'" % email
mycursor.execute(sql)
a=mycursor.fetchone()
print(a)
# fetchone: It is a method that is used when you want to select only the first row rom the table. it will return
# only one row from mysql


# school
# fetch the data of student using id

