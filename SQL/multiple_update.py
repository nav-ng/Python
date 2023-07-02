import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor = mydb.cursor()
id = int(input("Enter id of the person to be updated:"))
email = input("Enter new email:")
phone = int(input("Enter new phone number:"))
sql = "update person set email='%s', phone='%d' where id='%d'" % (email, phone, id)
mycursor.execute(sql)
mydb.commit()
print("Multiple values are updated")
