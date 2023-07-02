import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor = mydb.cursor()
name = input("Enter name to search:")
sql = "select * from person where name='%s'" % name
mycursor.execute(sql)
a = mycursor.fetchall()
for i in a:
    id = i[0]
    name = i[1]
    phone = i[2]
    email = i[3]
    print("id", id, "name", name, "phone", phone, "email", email)
