import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor = mydb.cursor()
column = input("Enter new column name:")
datatype = input("Enter datatype of new column:")
sql = "alter table student add %s %s" % (column, datatype)
mycursor.execute(sql)
mydb.commit()
print("Successfully added")
