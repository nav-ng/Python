import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
sql = "select max(mark) as smallestmark from student"
mycursor.execute(sql)
a = mycursor.fetchone()
print("Largest mark is", a)
