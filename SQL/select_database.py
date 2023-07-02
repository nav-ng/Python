import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor = mydb.cursor()
sql = "select * from person"
# * is a universal symbol that is used to select all datas
mycursor.execute(sql)
a = mycursor.fetchall()
# fetchall: it is used to fetch all datas and return a list of tuple
# [(1,amal,xyz), (2,sumal,abc)]
for i in a:
    id = i[0]
    name = i[1]
    phone = i[2]
    email = i[3]
    print("id", id, "name", name, "phone", phone, "email", email)

