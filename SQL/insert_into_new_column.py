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
    division = input("Enter the division:")
    sql = "update student set division='%s' where id=%d" % (division, id)
    mycursor.execute(sql)
    mydb.commit()
print("Data update complete")
