import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor = mydb.cursor()

sql = "create table person(id int auto_increment,name varchar(50),phone bigint(10),email varchar(50),primary key(id))"
mycursor.execute(sql)
mydb.commit()
print("Table created successfully")

# commit: It refers to the saving of data permanently after a set of changes
# primary key: It is a column that  contain values that uniquely identifying each row in a table

