import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor=mydb.cursor()
sql="select * from person order by name desc"
mycursor.execute(sql)
a=mycursor.fetchall()
for i in a:
    id=i[0]
    name=i[1]
    phone=i[2]
    email=i[3]
    print("id=",id,"name",name,"phone",phone,"email",email)


# sort school database by mark in descending order sort by name
