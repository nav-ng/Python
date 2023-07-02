import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"
)
my_cursor = mydb.cursor()
sql = "create table items(id int auto_increment,product varchar(100),price bigint(9),primary key(id))"
my_cursor.execute(sql)
mydb.commit()
print("Items table created successfully")
