# Write a Python program that accepts the user's first and last name and
# prints them in reverse order with a space between them?
# f_name = input("Enter your first name: ")
# l_name = input("Enter your last name: ")
# print(l_name[::-1] + " " + f_name[::-1])


# Write a Python program that accepts a sequence of comma-separated
# string from the user and generates a list and a tuple of those numbers.?
# new_string = "1,2,3,4,5"
# new_list = list(new_string.split(','))
# new_tuple = tuple(new_list)
# print(new_string)
# print(new_list)
# print(new_tuple)


# Write a Python program that prints the calendar for a given month and
# year.?
# import calendar
#
# year = 2022
# month = 2
# print(calendar.month(year, month))


# Write a Python program to sum two given integers. However, if the sum
# is between 15 and 20 it will return 20?
# def num_sum(num1, num2):
#     sum = num1 + num2
#     if 15 < sum < 20:
#         return 20
#
#
# print(num_sum(17, 0))


# Write a Python program to retrieve the path and name of the file
# currently being executed?
# import os
#
# print(os.getcwd())


# Write a Python program to sort three integers without using conditional
# statements and loops?
# num1 = 4
# num2 = 1
# num3 = 6
# ans_list=[num1,num2,num3]
# x=max(ans_list)
# y=min(ans_list)
# z=(num1+num2+num3)-(x+y)
# print("sorted numbers:",y,z,x)


# # Write a Python program to check whether a string is numeric.?
# new_string = "24"
# print(new_string.isnumeric())


# Write a Python function to find the maximum and minimum numbers
# from a sequence of numbers.?
# def max_min(list):
#     max_value=max(list)
#     min_value=min(list)
#     return "max value is: %d and min value is: %d" % (max_value, min_value)
#
#
# ans = max_min([2, 5, 1, 7, 9])
# print(ans)


# Write a Python program to check whether lowercase letters exist in a
# string?
# new_string = "HAi"
# flag = 0
# for i in new_string:
#     if i.islower():
#         flag = 1
#         break
# if flag == 1:
#     print("lowercase letter found")
# else:
#     print("no lowercase letter found")


# Write a Python program to filter positive numbers from a list using
# lambda ?
# num = [34, 1, 0, -23, 12, -88]
# ans = list(filter(lambda i: (i > 0), num))
# print(ans)


# Create a Vehicle class without any variables and methods?
# class Vehicle:
#     pass


# Create a private member function and access the method using name
# mangling?

# class Vehicle:
#     def f1(self, registration_no):
#         self.__reg_no = registration_no
#
#
# obj1 = Vehicle()
# obj1.f1("KL18C6679")
# print(obj1._Vehicle__reg_no)


# Create a abstraction class vehicle with 3 child classes?
# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#     @abstractmethod
#     def details(self):
#         pass
#
#
# class MarutiSuzuki(Vehicle):
#     def details(self):
#         print("Founded: 24 February 1981")
#         print("Headquarters: New Delhi")
#
#
# class TataMotors(Vehicle):
#     def details(self):
#         print("Founded: 1945")
#         print("Headquarters: Mumbai")
#
#
# class HindustanMotors(Vehicle):
#     def details(self):
#         print("Founded: 1942")
#         print("Headquarters: Chennai")
#
#
# car1 = MarutiSuzuki()
# car1.details()
# car2 = TataMotors()
# car2.details()
# car3 = HindustanMotors()
# car3.details()

# Explain types of inheritances with a coding example?
# single inheritance
# class school:
#     def s_details(self, s_name):
#         self.name = s_name
#         print("school:", self.name)
#
#
# class teacher(school):
#     def t_details(self, t_name):
#         self.name = t_name
#         print("teacher:", self.name)
#
#
# obj = teacher()
# obj.s_details("Luminar")
# obj.t_details("Anshya")

# multiple inheritance
# class school:
#     def s_details(self, s_name):
#         self.name = s_name
#         print("school:", self.name)
#
#
# class teacher:
#     def t_details(self, t_name):
#         self.name = t_name
#         print("teacher:", self.name)
#
#
# class student(school, teacher):
#     def std_details(self, std_name):
#         self.name = std_name
#         print("student:", self.name)
#
#
# obj = student()
# obj.std_details("amal")
# obj.t_details("Anshya")
# obj.s_details("Luminar")
# multilevel inheritance
# class school:
#     def s_details(self, s_name):
#         self.name = s_name
#         print("school:", self.name)
#
#
# class teacher(school):
#     def t_details(self, t_name):
#         self.name = t_name
#         print("teacher:", self.name)
#
#
# class student(teacher):
#     def std_details(self, std_name):
#         self.name = std_name
#         print("student:", self.name)
#
#
# obj = student()
# obj.std_details("amal")
# obj.t_details("Anshya")
# obj.s_details("Luminar")
# hierarchical inheritance
# class school:
#     def s_details(self, s_name):
#         self.name = s_name
#         print("school:", self.name)
#
#
# class teacher(school):
#     def t_details(self, t_name):
#         self.name = t_name
#         print("teacher:", self.name)
#
#
# class student(school):
#     def std_details(self, std_name):
#         self.name = std_name
#         print("student:", self.name)
#
#
# obj1 = teacher()
# obj1.s_details("Luminar")
# obj1.t_details("Anshya")
# obj2 = student()
# obj2.s_details("CEK")
# obj2.std_details("Amal")
# hybrid inheritance
# class university:
#     def u_details(self, u_name):
#         self.name = u_name
#         print("university:", self.name)
#
#
# class school(university):
#     def s_details(self, s_name):
#         self.name = s_name
#         print("school:", self.name)
#
#
# class course(university):
#     def c_details(self, c_name):
#         self.name = c_name
#         print("course:", self.name)
#
#
# class student(school, course):
#     def std_details(self, std_name):
#         self.name = std_name
#         print("student:", self.name)
#
#
# obj = student()
# obj.u_details("KTU")
# obj.s_details("CEK")
# obj.c_details("CS")
# obj.std_details("Amal")

# Create 3 user defined exception classes (Exception handling)
# class Error(Exception):
#     pass
#
#
# class ErrorInputException(Error):
#     pass
#
#
# class ChildException(Error):
#     pass
#
#
# class OldException(Error):
#     pass
#
#
# try:
#     age = int(input("Enter your age:"))
#     if age != int(age):
#         raise ErrorInputException
#     elif age < 18:
#         raise ChildException
#     elif age > 60:
#         raise OldException
#     else:
#         print("Success")
# except ErrorInputException:
#     print("The input is not an integer")
# except ChildException:
#     print("The age is below 18")
# except OldException:
#     print("The age is above 60")


# write queries
# sql="create database school"
# sql="create table student(id int auto_increment, student_name varchar(50)), place varchar(50)"
# sql="select * from school"
# nm="Hari"
# new_id=2
# sql="update student set id=%d where student_name='%s'" %(new_id,nm)
# new_id=2
# sql="delete from student where id=%d" %(new_id)
# sql="alter table school add email varchar(50)"
# sql="drop database school"
# sql="drop table student0"
# sql="select min(id) from student"
# sql="select max(id) from student"
# sql="select name from student order by id decs"


# print(sum(range(1, 102)))
# list=[1,2,3,4,5,6,7,8,9,10]
# print(sum(list))


# find duplicates in an array

# def duplicates(array):
#     dup = []
#     check=[]
#     for i in array:
#         if i in check and i not in dup:
#             dup.append(i)
#         else:
#             check.append(i)
#     # for i in range(len(array) - 1):
#     #     for j in range(i + 1, len(array) - 1):
#     #         if array[i] == array[j] and array[j] not in dup and array[j] <= len(array) - 1:
#     #             dup.append(array[j])
#     return dup
#
#
# list1 = [12, 14, 15, 12, 7, 4, 9, 3, 7, 43, 3, 3, 43]
# print(duplicates(list1))


# rotation of array
# def rotation(array):
#     n = array[0]
#     a = array[n:len(array)]
#     b = array[0:n]
#     ans = a + b
#     str1 = ""
#     for i in ans:
#         str1 += str(i)
#     return str1
#
#
# list1 = [2, 3, 4, 5, 6, 7, 8]
# print(rotation(list1))


# for i in range(1, 5):
#     if i % 2 != 0:
#         for j in range(1):
#             print("*")
#         for k in range(4 * i):
#             print("*", end="")
#         print()
#     else:
#         for j in range(3):
#             print("*")
#         for k in range(4 * i):
#             print("*", end="")
#         print()


# for i in range(1,5):
#     for j in range(i+1):
#         print("*", end="")
#     print()
#     if i==4:
#         break
#     for k in range(i):
#         print("*")

# for i in range(1,4):
#     for j in range(1,4):
#         if j!=3:
#             for k in range(3*i):
#                 print("*", end=" ")
#             print()
#         else:
#             if i==3:
#                 break
#             for k in range(3*i+i):
#                 print("*", end=" ")
#             print()

#count of prime numbers in a list

# list1=[1,3,5,7,2,7,4,90,1,65,3,87,3,1,0]
# count=0
# for i in list1:
#     flag=0
#     if i!=0 and i!=1:
#         if i==2:
#             count+=1
#         else:
#             for j in range(2,i):
#                 if i%j==0:
#                     flag=1
#             if flag==0:
#                count+=1
# print(count)



# n= 5
# for i in range(n):
#     for j in range(n-i-1,0,-1):
#         print(" ", end=" ")
#     for k in range(2*i+1):
#         print("*", end=" ")
#     print()






































