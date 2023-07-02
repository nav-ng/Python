import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor = mydb.cursor()
id = int(input("Enter id to be updated:"))
name = input("Enter name to be updated:")
email = input("Enter new email:")
sql = "update person set email='%s' where id=%d and name='%s'" % (email, id, name)
mycursor.execute(sql)
mydb.commit()
print("Updated")
