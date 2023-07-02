import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
number = int(input("Enter the number of student:"))
for i in range(number):
    std_name = input("Enter student name:")
    school_name = input("Enter school name:")
    roll_no = int(input("Enter roll number:"))
    department = input("Enter department:")
    mark = int(input("Enter mark:"))
    sql = "insert into student(student_name,school_name,roll_number,department,mark) values('%s','%s',%d,'%s',%d)" % (std_name, school_name, roll_no, department, mark)
    mycursor.execute(sql)
mydb.commit()
print("Data added successfully")
