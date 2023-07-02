import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
sql = "select sum(mark) from student"
mycursor.execute(sql)
a = mycursor.fetchone()
b = a[0]
print("The sum of mark is", b)