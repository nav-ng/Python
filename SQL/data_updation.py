import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor = mydb.cursor()
id = int(input("Enter the id:"))
name = input("Enter new name:")
sql = "update person set name='%s' where  id=%d" % (name, id)
mycursor.execute(sql)
mydb.commit()
print("Database updated")
