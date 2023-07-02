import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
sql = "select avg(mark) from student"
mycursor.execute(sql)
a = mycursor.fetchone()
b = a[0]
print("The average of mark is", b)