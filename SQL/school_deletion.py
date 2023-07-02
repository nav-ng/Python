import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
name = input("Enter the name:")
sql = "delete from student where student_name='%s'" % name
mycursor.execute(sql)
mydb.commit()
print("Delete successfully")
