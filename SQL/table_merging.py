import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"
)
my_cursor = mydb.cursor()
sql = "select items.id, items.product, items.price, customer.purchase_date, customer.customer_name from items inner join customer on items.id=customer.id"
my_cursor.execute(sql)
a = my_cursor.fetchall()
for i in a:
    id = i[0]
    product = i[1]
    price = i[2]
    date = i[3]
    name = i[4]
    print("ID:", id, "Product:", product, "Price:", price, "Date:", date, "Name:", name)
mydb.commit()

