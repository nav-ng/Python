# # syntax
# # def function_name():  #function declaration
# #     print("Hello")    #function definition
# #     .......
# #     .......
# #
# # function_name()       #function calling
# #
# #  write a program to add two numbers using function
#
# def add():
#     num1 = int(input("Enter 1st number: "))
#     num2 = int(input("Enter 2nd number: "))
#     print(num1 + num2)
# add()
#
# # function with argument
# # what is an argument?
# # The term argument or parameter can be used for passing information into a function.
#
# # write a program to add two numbers using function with argument
#
# def add(num1, num2):
#     print(num1 + num2)
# add(1, 2)
#
# # write a program to find factorial of a number using function with argument?
#
# def factorial(num):
#     fact = 1
#     for i in range(num):
#         fact = (fact * (num-i))
#     print(fact)
#
#
# factorial(4)
#
# # write a program to find reverse of a number using function?
#
# def reverse(num):
#     rev = 0
#     temp = num
#     while num > 0:
#         rem = num % 10
#         rev = rev * 10 + rem
#         num //= 10
#     print("The reverse of number", temp, "is", rev)
#
#
# reverse(123)
#
# # write a program to find reverse of a string using function
#
# def reverse_of_string(string):
#     string1 = string[::-1]
#     print(string1)
#
#
# reverse_of_string("malayalam")
#
# # write a program to generate multiplication table using function
#
# def multiplication(num):
#     for i in range(1,11):
#         print(num, "x", i, "=", num * i)
#     print()
#
#
# multiplication(2)
#
# # function with return type
#
# def hello():
#     return "hello"
#
#
# print(hello())
#
# # add 2 numbers using function with argument and return type
#
# def add(num1, num2):
#     return num1 + num2
#
#
# print(add(2, 3))
#
# # write a program to find the number is armstrong or not using function with argument and return type
#
# def armstrong(num):
#     arm = 0
#     temp = num
#     while num > 0:
#         rem = num % 10
#         arm = arm + rem ** 3
#         num //= 10
#     if temp == arm:
#         return "True"
#     else:
#         return "False"
#
#
# print(armstrong(153))
#
# # print a number is even or odd using function with argument and return type
#
# def odd_or_even(num):
#     if num % 2 == 0:
#         return "%d is even" % num
#     else:
#         return "%d is odd" % num
#
#
# print(odd_or_even(5))
#
# # find the smallest of 5 numbers using function with argument and return type
#
# def smallest(num1, num2, num3, num4, num5):
#     if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
#         return num1
#     elif num2 > num3 and num2 > num4 and num2 > num5:
#         return num2
#     elif num3 > num4 and num3 > num5:
#         return num3
#     elif num4 > num5:
#         return num4
#     else:
#         return num5
#
#
# z = smallest(12, 13, 1, 6, 2)
# print("The greatest number is", z)
#
# # formatters:
# # %s-string formatters
# # %d-number formatters
# # %f-float formatters
#
# # write a python program to print even numbers from the given list
#
# def even(list1):
#     list2 = []
#     for i in list1:
#         if i % 2 == 0:
#             list2.append(i)
#     return list2
#
#
# print(even([2, 3, 4, 5, 6, 1, 8, 9]))
#
# # write a program to print positive numbers and negative numbers from a given list using function
#
# def positive_or_negative(list1):
#     positive_list = []
#     negative_list = []
#     for i in list1:
#         if i > 0:
#             positive_list.append(i)
#         else:
#             negative_list.append(i)
#     return negative_list, positive_list
#
#
# print(positive_or_negative([2, 3, 6, 4, 8, -1, -5, -4, -2, -5, 8]))


# what is a return type?
# a return type statement ends the execution of a function and returns value to the calling function.
