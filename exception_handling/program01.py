# try:
#   a=int(input("Enter first number:"))
#   b=int(input("Enter second number:"))
#   c=a/b
#   print(c)
# except:
#    print("Can't divide a number by zero")

# solve quadratic equation using try and except block.
# a=int(input("Enter coefficient of x^2 number:"))
# b=int(input("Enter coefficient of x number:"))
# c=int(input("Enter coefficient of x^0 number"))
# d=((b**2)-(4*a*c))**0.5


# try:
#     x1=(-b+d)/(2*a)
#     x2=(-b-d)/(2*a)
#     print("Solutions are",x1,x2)
#
# except:
#     print("Can't divisible a number by zero")

# value error
# try:
#     a = int(input("Enter a number:"))
#     print(a)
# except:
#     print("Please input an integer number")

# file not found error
# import os
# try:
#     os.remove(r"C:\Users\nav_ng\Desktop\New folder (2)\hi2.txt")
#     print("removed")
# except:
#     print("File does not exist")

# Name Error
# try:
#     a = int(input("Enter a number:"))
#     print(b)
# except:
#     print("Temporary variable is not declared")

# index error:
# list=['a','b','c']
# try:
#     print(list[0])
#     print(list[3])
# except:
#     print("index position out of range")

# multiple errors
# try:
#     a = int(input("Enter the value of a:"))
#     b = int(input("enter the value off b:"))
#     c = a / b
#     print(c)
# except ValueError:
#     print("Value error occurred")
# except ZeroDivisionError:
#     print("Zero division error occurred")
# except NameError:
#     print("Name error occurred")
# except Exception:
#     print("Something went wrong")


# Exception with arguments: An exception can have an argument which gives a value that gives additional information
# about the problem. the content of the argument vary by exception.

# try:
#     a = int(input("Enter the value of a:"))
#     b = int(input("enter the value off b:"))
#     c = a / b
#     print(c)
# except ValueError as a:
#     print(a)
# except ZeroDivisionError as b:
#     print(b)
# except NameError as c:
#     print(c)
# except Exception:
#     print("Something went wrong")

# raise keyword:Python raise keyword which is used to raise exception or errors. The raise keyword raise an error and
# stop the control flow of the program.

# try:
#     name=input("enter name:")
#     age=int(input("Enter age:"))
#     if age>=18:
#         print("Eligible")
#     elif age<18:
#         raise Exception
#
# except ValueError as e:
#     print(e)
# except Exception:
#     print("Age is not valid")

# positive_negative

# try:
#     num = int(input("Enter a number:"))
#     if num >= 0:
#         print(num, "is a positive number")
#     elif num < 0:
#         raise Exception
#
# except ValueError as a:
#     print(a)
# except Exception:
#     print("Negative exception")

# try except else block:
# Syntax:
# try:
#     code to be executed
# except:
#     code execute if error occurs
# except:
#     code
#     execute if error occurs
# else:
#     if there is no exception then execute this block

# try:
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     c = a / b
#     print(c)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print("Division completed successfully")

# try except-finally block:
# try:
#     code to be executed
# except:
#     code execute if error occurs
# except:
#     code execute if error occurs
# else:
#   print("Division completed")
# finally:
#     executes the block if an error occurs or not
# the final keyword is used in try except block it defines a block of  code to run the try except block is final.

# user defined exception: in python user can define custom exception by creating a new class. this exception class to
# be derived either directly or indirectly. from the built-in exception class most of the built-in exceptions are also
# derived from this class

# class Error(Exception):  # main child class
#     pass
#
#
# class ZeroError(Error):  # child class
#     pass
#
#
# try:
#     num=int(input("Enter a number:"))
#     if num==0:
#         raise ZeroError
# except ZeroError:
#     print("Input value is zero, try again")


# class Error(Exception):
#     pass
#
#
# class NegativeException(Error):
#     pass
#
#
# class ZeroValueException(Error):
#     pass
#
#
# try:
#     num = int(input("Enter 1st number:"))
#     if num < 0:
#         raise NegativeException
#     elif num == 0:
#         raise ZeroDivisionError
#     else:
#         print("Its a positive number")
#
# except NegativeException:
#     print("Its a negative value")
# except ZeroValueException:
#     print("Its a zero")
# finally:
#     print("Complete")
