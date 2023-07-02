import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor=mydb.cursor()
id=int(input("Enter id to be deleted:"))
sql="delete from person where id=%d"%(id)
mycursor.execute(sql)
mydb.commit()
print("Delete succefully")


# delete using name database school
# delete using department and roll no