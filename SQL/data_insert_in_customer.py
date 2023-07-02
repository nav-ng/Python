import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"
)
my_cursor = mydb.cursor()
num = int(input("Enter the number of data to be inserted:"))
for i in range(num):
    date = input("Enter the date:")
    name = input("Enter the customer name:")
    sql = "insert into customer(purchase_date,customer_name) values('%s','%s')" % (date, name)
    my_cursor.execute(sql)
    mydb.commit()
print("Data insertion successful")
