# in python, it is the process of wrapping up methods and variables into a single unit.
# it acts as a protective layer by ensuring that access to wrapped data is not possible by any code defined
# outside the class.
# it hides data to be modified from outside world.
# access modifiers:
# Public members: access anywhere from  outside the class
# protected members: accessible within the class and subclass
# private members: accessible within the class

# data hiding using encapsulation
# class employee:
#     def __init__(self, name, project, salary):
#         self.name = name  # public
#         self._project = project  # protected
#         self.__salary = salary  #private


# create public method

# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#         print(self.name)
#         print(self.__salary)
# #
# #
# obj1 = employee("Amal", 10000)
#
# print(obj1.name)
# print(obj1.__salary)


# AttributeError: "employee object has no attribute "__salary"

# two methods to access private data members
# 1.name mangling
# _classname__datamember
# classname is the current class and data member is the private variable name.

# 2.Using public method to access private data member

# class employee:
#     def f1(self, name, salary):
#         self.name = name
#         self.__salary = salary
#     def f2(self):
#         print(self.name)
#         print(self.__salary)
#
#
# obj1 = employee()
# obj1.f1("Amal",10000)
# obj1.f2()

# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#     def f2(self):
#         print(self.name)
#         print(self.__salary)
#
#
#
# obj1 = employee("Amal", 10000)
# obj1.f2()

# protected access modifier:

class employee:
    def __init__(self, name, project):
        self.name = name
        self._project = project


class person(employee):
    def __init__(self, name, project, pname):
        employee.__init__(self, name, project)
        self.nm=pname


obj = person("Alex", "E-Rationcard", "alex john")
print(obj.name)
print(obj._project)
print(obj.nm)
