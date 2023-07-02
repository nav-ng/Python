import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
department = input("Enter the department:")
roll_no=int(input("Enter roll no:"))
sql = "delete from student where department='%s' and roll_number=%d" % (department,roll_no)
mycursor.execute(sql)
mydb.commit()
print("Delete successfully")
