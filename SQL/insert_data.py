import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor = mydb.cursor()
num = int(input("Enter the number of person:"))
for i in range(num):
    nm = input("Enter your name:")
    ph = int(input("Enter your phone number:"))
    mail = input("Enter your email:")
    sql = "insert into person(name,phone,email) values('%s',%d,'%s')" % (nm, ph, mail)
    mycursor.execute(sql)
mydb.commit()
print("Data added successfully")
