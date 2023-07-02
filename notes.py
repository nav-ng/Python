# advanced python
# oops concept: oops that stand for object-oriented programing oop language allows to break the
# program into the bit-sized program that can be solved easily it help to write the cleaner code and to maintain
# control over the function and modules. oops works on the principle of class, object, abstraction, encapsulation,
# polymorphism, inheritance.
# table sorting
# count() it will return the count of a specific column
# sql="select count(column name)from table name"
# avg() it will return the average value form a numeric column
# sql="select sum(column name) from table name"
# sum() it will return the sum of a specific column.
# sql="select avg(column name) from table name"
# sql="alter table table_name column_name datatype"
# how to remove a column from an existing table
# sql="alter table table_name drop column column_name"
# query to delete data :
# sql="drop table table_name"
# query to delete a database:
# sql="drop database database_name"
# shop database
# items and customer tables
# id, product, price
# id, purchased_date, customer_name
# two join two tables in the same database:
# sql="select items.id, items.product,customers.purchased_date,customer.customer_name from items inner join customers on
# inner join customer on items.id=customer.id"
# mycursor.execute(sql)
# c=mycursor.fetchall()
# for i in c:
#     id=i[0]
#     product[1]
#     data=i[2]
# in python, it can be handled using try statement.
# Exception: unwanted errors occurs during the runtime of a program.
# exceptions are raised when the program is synthetically correct but the code resulted in an error.
# This error does not stop the execution of the programmer, however it changes the normal flow of the program.
# we can classify error into 2 types
# 1.syntax Errors: the error that made by the programmer in program syntax.
# 2.runtime Error: End user errors.
# common exceptions:
# 1.ZeroDivisionError: This error occurs when a number is divided by zero.
# NameError: It occurs when a name is not found, It may local or global.
# IndentationError: It occurs when incorrect indent is given.
# FileNotFoundError: It occurs when a file doesn't exist.
# ValueError: When an incorrect value given by the End user.

# multithreading:
# what is a process:
# what is a thread: a thread is a part of a process.
# process: It is heavyweight, each process has its own memory and file resources,
# thread: it needs a direct interaction with the process, all thread that shares same set of memory and file resources
# types of thread:
# Threads are being classified into two types
# 1.Single thread: One process at a time, works in a main thread
# 2.MultithreadL: Multiple threads at a time, Divides a process into child threads.
# beneficent of multithreading:
# it saves time, less memory space required, It ensures effective utilisation of computer system resources


# HTML stands for hypertext markup language
# it is the slandered markup language for creating webpages
# it describes the structure ofa webpage.
# it consists of a series of element.
# this element tells the browser how to display the content.
# html heading tags:
# h1, h2, h3, h4, h5, h6.
# h1:Most using heading tag
# h6:Least using heading tag
# align property have right, left, center, justify
# paragraph tag-p tag
# anchor tag: to create hyperlinks in html pages
# href: it stands for hypertext reference
# <a href="image.jpg">download>Click me to download</a>
# img tag: to insert a image
# empty elements:tags without closing
# src: source
# unordered list: disc, square, circle, none
# >> bit-wise right shift
# python is scalable because we can do large and small program using python with its quality such as build in data
# structure and dynamic binding and dynamic typic.
# the source code of a python program is converted into byte code that is then executed by the python virtual machine.

# value attributes: it specifies the value of an element it is used differently for different input types.
# for button reset and submit it define the text on the button.
# for text password and other input field it defines a default value
# placeholder:it acts as a hint
# read only attribute eg: value
# html methods:
# they are classifies into two types
# 1-post method
# 2-get method
# the get and post methods that are used to transfer data from the client to the server
# get is less secure compared to post because data send as a part of url
# required attribute: it is required
# action: It is an attribute used in html form that specifies where to send the form data when a form is submitted
# <input> size attribute:size=10
# bgcolor attribute:
# a company decided to give bonous of 5 person to employee if his or her service is more than 5 year ask the user for
# their salary and service and print the bonus
# CSS: cascading style sheet which is used to style html elements
# it is classified into 3 types
# 1.inline css
# 2.internal css
# 3.external css
