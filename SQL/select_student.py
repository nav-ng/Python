import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
id = int(input("Enter id to be searched:"))
sql = "select * from student where id=%d" % id
mycursor.execute(sql)
a = mycursor.fetchone()
print(a)
