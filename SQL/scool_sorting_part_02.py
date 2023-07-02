import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
sql = "select * from student order by student_name"
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
