# it is a method or operator that can do different functionality with the same name and different parameters.
class a:
    def product(self, a, b):
        print(a + b)

    def product(self, c, d, e):
        print(c + d + e)


obj1 = a()
obj1.product(1, 2)
obj1.product(1, 2, 3)

# In the above code we have defined two product method, but we can only use the second product method as python does
# not support method overloading.

# 2 methods to achieve method overloading in python
# 1.first method to achieve method overloading
# answer = 0


# def add(datatype, *args):
#     global answer
#     if datatype == int:
#         answer = 0
#     if datatype == 'str':
#         answer = ''
#     for x in args:
#         answer = answer + x
#     print(answer)
#
#
# add('int', 5, 6, 6, 7, 8, 8)
# add('str', 'hi', 'geeks', 'hello', 'hi')

# 2.Multiple dispatch method

# how to install package in python
# pip install package
# here pip that stands for preferred installer package
#

# from multipledispatch import dispatch
#
#
# class a:
#     @dispatch(int, int, int, int)
#     def product(self, first, second, third, fourth):
#         result = first * second * third * fourth
#         print(result)
#
#     @dispatch(str, str, str, str, str)
#     def product(self, first, second, third, fourth, five):
#         result = first + second + third + fourth + five
#         print(result)
#
#     @dispatch(float, float, float)
#     def product(self, a, b, c):
#         result = a + b + c
#         print(result)
#
#
# obj = a()
# obj.product(1, 2, 3, 4)
# obj.product('hello', 'hai', 'welcome', 'aa', 'bb')
# obj.product(1.3, 1.4, 1.5)

