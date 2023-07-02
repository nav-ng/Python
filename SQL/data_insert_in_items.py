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
    product = input("Enter the name of product:")
    price = int(input("Enter the price:"))
    sql = "insert into items(product,price) values('%s',%d)" % (product, price)
    my_cursor.execute(sql)
    mydb.commit()
print("Data insertion successful")
