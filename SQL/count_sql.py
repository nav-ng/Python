import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
sql = "select count(student_name) from student"
mycursor.execute(sql)
a = mycursor.fetchone()
b = a[0]
print("The count is", b)
