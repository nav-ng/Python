import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
name = input("Enter the name:")
mark = int(input("Enter the new mark:"))
sql = "update student set mark=%d where student_name='%s'" % (mark, name)
mycursor.execute(sql)
mydb.commit()
print("Value updated")
