import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
sql = "create table student(id int auto_increment,student_name varchar(50),school_name varchar(100),roll_number int ,department varchar(100),mark int, primary key(id)) "
mycursor.execute(sql)
mydb.commit()
print("Table created successfully")
