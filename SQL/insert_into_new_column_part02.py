import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
num = int(input("Enter how many element you adding:"))
for i in range(num):
    id = int(input("Enter the id:"))
    attendance = input("Enter the attendance:")
    sql = "update student set attendance='%s' where id=%d" % (attendance, id)
    mycursor.execute(sql)
    mydb.commit()
print("Data update complete")