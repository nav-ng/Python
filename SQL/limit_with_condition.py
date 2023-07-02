# the limit clause which is used to specify the number of records to return
# sql="select * from table name limit %d"%(lim)
# sql="select * from table name where name='%s' limit %d"%(name,limit)

import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
name = input("Enter the name:")
limit = int(input("Enter the limit:"))
sql = "select * from student where student_name='%s' limit %d" % (name, limit)
mycursor.execute(sql)
a = mycursor.fetchall()
for i in a:
    id = i[0]
    student_name = i[1]
    school_name = i[2]
    roll_number = i[3]
    department = i[4]
    mark = i[5]
    print("Id:", id, "Student name:", student_name, "School name:", school_name, "Roll number:", roll_number,"Department:", department, "Mark:", mark)
