import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"
)
my_cursor = mydb.cursor()
sql = "create table customer(id int auto_increment,purchase_date date,customer_name varchar(50), primary key(id))"
my_cursor.execute(sql)
mydb.commit()
print("Customer table created successfully")
