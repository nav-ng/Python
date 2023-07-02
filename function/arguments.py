# types of arguments
# 1.Arbitrary arguments
# 2.Keyword arguments
# 3.Arbitrary keyword argument
# 4.Default argument

# 1.Arbitrary arguments

# def add(*args):
#     for i in args:
#         print(i)
#
#
# add(1, 4, 2, 5, 7, 0, 2)

# write a program to add numbers using *args

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#         print(i, "\b+", end="")
#     print('\b', "=", sum)
#
#
# add(1, 2, 3, 4, 5, 6)


# write a program to multiply numbers using args

# def multiply(*args):
#     mul = 1
#     for i in args:
#         mul *= i
#         print(i, "x", end=" ")
#     print("\b\b""=", mul)
#
#
# multiply(1, 2, 3, 4)

# 2.keyword arguments: they are values that when passed into a function are identifiable by specific parameters

# def name(last_name, first_name, middle_name):
#     print(first_name, "\t", middle_name, "\t", last_name)
#
#
# name(first_name="f_name", last_name="l_name", middle_name="m_name")

# 3.Arbitrary keyword arguments

# if you don't know how many keyword arguments that will be passed into your function add two star before the parameter.

# def abc(**kwargs):
#     print(kwargs['a'])
#     print(kwargs['b'])
#     print(kwargs['c'])
#     print(kwargs['d'])
#
#
# abc(a="alex", b="amal", c="arun", d="xyz", e="abc")

# iteration in **kwargs
# iteration of keys

# def abc(**a):
#     for i in a:
#         print(i)
#
#
# abc(a=10, b=20, c=30)


# iteration of values

# def abc(**a):
#     for i in a.values():
#         print(i)
#
#
# abc(a=10, b=20, c=30)


# item(): the item method that returns a view object that contains a key value pair.

# def abc(**a):
#     for i, j in a.items():
#         print(i, ' ', j)
#
#
# abc(a=10, b=20, c=30)


# 4.default arguments: default values indicates that the function arguments will take values if no arguments is
# passed during the function call.

# def abc(a, b, c=0):
#     print(a + b + c)
#
#
# abc(2, 4)


# def largest(a, b, c=0, d=0):
#     if a > b and a > c and a > d:
#         print(a)
#     elif b > c and b > d:
#         print(b)
#     elif c > d:
#         print(c)
#     else:
#         print(d)
#
#
# largest(20, 30, 40, 50)


# scope of variable:
# global variable:a variable that is declared outside the function that can access anywhere in the program
# local variable: a variable that is declared inside a function that can't access from outside a function

# global variable

# a = 100
# #
# #
# def abc():
#     print(a)
#
#
# abc()
# print(a)

# local variable

# def abc():
#     a = 100
#     print(a)
#
#
# abc()

# global keyword: in python global keyword allows you to modify the variable outside the function. it is used to
# create a global variable and make changes to the variable in local context.

# a=10
# def abc():
#     global a
#     a+=1
#     print(a)
#
# abc()

# lambda function: it is an anonymous function used for a short period of time.
# anonymous function: a function without declaration.
# syntax

# variable name=lambda argument:expression

# def add(a,b):
#     print(a+b)
#
# add(1,2)

# x = lambda a, b: a + b
# print(x(1, 2))

# x = lambda a, b, c: a / b * c
# print(x(10, 1, 2))


# x = lambda a: a ** 0.5
# print(x(4))


# x = lambda num: num ** 3
# print(x(3))

# x = lambda height, length: 0.5 * height * length
# print(x(2, 3))


# lambda build in function
# filter()
# map()
# reduce()

# lambda with filter
# that takes a list as an argument
# this will filter out all the element in a sequence
# syntax
# variable name= list(filter(lambda argument:expression, variable name of list)))

# filter odd number from the list list1=[1,2,3,4,5,6,7,8,9,10]
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = list(filter(lambda i: (i % 2 != 0), list1))
# print(a)


# filter even numbers from the list li=[100,110,22,54,1,43,101,222]

# li = [100, 110, 22, 54, 1, 43, 101, 222]
# a = list(filter(lambda i: (i % 2 == 0), li))
# print(a)


# from the given list filter out number which is divisible by 13 but not by 3, li=[1,213,100,220,101,33,13]

# li = [1, 213, 100, 220, 101, 33, 13]
# a = list(filter(lambda i: (i % 13 == 0 and i % 3 != 0), li))
# print(a)

# age=[12,34,28,2,50,22,1], from the given list filter out ages between 18 and 50

# age = [12, 34, 28, 2, 50, 22, 1]
# a = list(filter(lambda i: (i > 18 and i < 50), age))
# print(a)

# from the list li=[1,-2,12,2,3,-6,0,0] filter out positive number and negative number and zero as 3 separate lists

# li = [1, -2, 12, 2, 3, -6, 0, 0]
# a = list(filter(lambda i: i > 0, li))
# b = list(filter(lambda i: i < 0, li))
# c = list(filter(lambda i: i == 0, li))
# print(a, b, c)

# map(): it takes a list as an argument and a new list is return. it is a build in function that allows you to
# process and transform all the items in an iterable list without a for loop.
# syntax
# variable name=list(map(lambda argument:expression,variable of list))

# li = [1, 2, 3, 4, 5]
# a = list(map(lambda i: (i ** 2), li))
# print(a)

# find the square root of each element in a list

# li = [4, 9, 16, 25]
# a = list(map(lambda i: (i ** 0.5), li))
# print(a)


# create a list from 1 to 10,
# input enter a number: 5
# output multiplication table values as a list


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = int(input("Enter a number: "))
# a = list(map(lambda i: num * i, list1))
# print(a)


# lambda using conditional statement

# square = lambda x: x ** 2 if (x > 0) else None
# num = int(input("Enter a number: "))
# print(square(num))


# none is used to define a null value


# find the largest of 2 numbers using lambda

# largest = lambda a, b: "%d is largest" % a if (a > b) else "%d is largest" % b
# print(largest(2, 3))


# find the square root of a number if the number greater than zero

# num = int(input("Enter a number: "))
# square_root = lambda n: n ** 0.5 if (num > 0) else None
# print(square_root(num))


# convert a positive number into a negative number and a negative number to positive number using lambda

# sign-change = lambda x: 0 - x if (x > 0) else 0 - x
# num = int(input("Enter a number: "))
# print(sign-change(num))


# odd_or_even = lambda x: "%d is even" % x if (x % 2 == 0) else "%d is odd" % x
# num = int(input("Enter a number: "))
# print(odd_or_even(num))


# num = int(input("Enter a number: "))
# x = lambda i: i * 2 if (i <= 10) else i * 3
# print(x(num))


# eligibility = lambda x, string: "%s is eligible for vaccination" % string if (
#             x >= 18) else "%s is not eligible for vaccination" % string
# age = int(input("Enter your age: "))
# name = input("Enter your name: ")
# print(eligibility(age, name))


# largest = lambda a, b, c: "%d is largest" % a if (a > b and a > c) else (
#     "%d is largest" % b if (b > c) else "%d is largest" % c)
# print(largest(1, 2, 3))

#
# largest = lambda a, b, c: "%d is largest" % a if (a > b and a > c) else (
#     "%d is largest" % b if (b > c) else "%d is largest" % c)
# print(largest(2,3,6))
# write a lambda function to find the smallest of 4 number

# smallest = lambda a, b, c, d: "%d is smallest" % a if (a < b and a < c and a < d) else ("%d is smallest" % b if (b
# < c and b < d) else ("%d is smallest" % c if (c < d) else "%d is smallest" % d))
# print(smallest(4, 6, 2, 8))


# lambda reduced function
# a reduced function in python that takes a list as an argument and a new reduced result is return
# the reduced function which belongs to function tool module
# module is a collection of function
# from functools import reduce

# find the largest element from the list using reduce function

# from functools import reduce
#
# li = [100, 200, 300, 400, 500]
# max = reduce(lambda a, b: a if (a > b) else b, li)
# print(max)

# from functools import reduce
# li = [100, 200, 300, 400, 500]
# min = reduce(lambda a, b: a if (a < b) else b, li)
# print(min)


# find the sum of element in the list using reduce function
#
# from functools import reduce
#
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = reduce(lambda a, b: a + b, li)
# print(sum)

