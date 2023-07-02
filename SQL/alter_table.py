import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
sql = "alter table student add attendance int(5)"
mycursor.execute(sql)
mydb.commit()
print("Successfully completed")
