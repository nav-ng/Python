# syntax:
# class class_name:  # class declaration
#   def function_name(self):
#       body
# obj=class_name() # reference object
# obj.function_name()

# a function that is declared inside a class known as member function/method.
# self keyword: The self parameter is a reference to the current instance of the class.
# By using self keyword we can access the attributes and methods of the class in python.


# class person:
#     def setval(self, name, address, phone):
#         self.nm = name
#         self.add = address
#         self.ph = phone
#         print("name:", self.nm)
#         print("Address:", self.add)
#         print("Phone no:", self.ph)
#
#
# obj1 = person()
# obj1.setval("Antonio Gustavo", "ABC", 573965859)
# obj2 = person()
# obj2.setval("Thomas Shelby", "DEF", 7489367509)


# class person:
#     def setval(self, name, address, phone):
#         self.nm = name
#         self.add = address
#         self.ph = phone
#
#     def print_val(self):
#         print("name:", self.nm)
#         print("Address:", self.add)
#         print("Phone no:", self.ph)
#
#
# obj1 = person()
# obj1.setval("Antonio Gustavo", "ABC", 573965859)
# obj1.print_val()
# obj2 = person()
# obj2.setval("Thomas Shelby", "DEF", 7489367509)
# obj2.print_val()

# create a class car with arguments name,color, model
# create 3 object using class car.

# class car:
#     def set_value(self, car_name, car_color, car_model):
#         self.name = car_name
#         self.color = car_color
#         self.model = car_model
#
#     def print_value(self):
#         print("name:", self.name)
#         print("color:", self.color)
#         print("model:", self.model)
#
#
# obj1 = car()
# obj1.set_value("Dodge demon", "Black", 2021)
# obj1.print_value()
# obj2 = car()
# obj2.set_value("Nissan GTR", "Blue", 2002)
# obj2.print_value()
# obj3 = car()
# obj3.set_value("Toyota supra", "orange", 2014)
# obj3.print_value()


# Static variable and Dynamic variable

# A variable that declared inside a class but outside any method is called static variable.
# A variable that is declared inside a method that changes its value while creating an object
# is called dynamic variable.


# class company:
#     company_name = "TCS"
#
#     def employee(self, emp_name, emp_id, salary, email):
#         self.name = emp_name
#         self.id = emp_id
#         self.salary = salary
#         self.email = email
#         print("company name:", company.company_name, "Name:", self.name, "emp id:", self.id, "salary:", self.salary,
#               "email:", self.email)
#
#
# obj1 = company()
# obj1.employee("Alex", 12345, 10000, "alex@gmail.com", )


# create a class school
# school name and location are static
# create 3 student object
# roll no, department, name,


# class school:
#     school_name = "ABC school"
#     location_name = "London"
#
#     def student(self, name, roll_no, department):
#         self.name = name
#         self.roll_no = roll_no
#         self.department = department
#         print("school name:", school.school_name, "Location:", school.location_name, "Name:", self.name, "Roll no:",
#               self.roll_no, "Department: ", self.department)
#
#
# obj1 = school()
# obj1.student("Sumal", 6, "CSE", )
# obj2 = school()
# obj2.student("Amal", 7, "EC")
# obj3 = school()
# obj3.student("Vimal", 8, "CE")


# constructor: The constructor are generally used for initialize for assign values to the data members of the class
# when an object is created. the init method __init__() is called constructor, and it is always called when an object
# is created
# syntax
# def __init__():
#   body of constructor


# class person:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#         print("Name:", self.name, "Phone:", self.phone)
#
#
# obj1 = person("Amal", 8976354973)


# create a class laptop using constructor
# processor, color, os, memory
# 2 laptop object

# class laptop: def __init__(self, processor, color, os, memory): self.processor = processor self.color = color
# self.os = os self.memory = memory print("Processor:", self.processor, "Color:", self.color, "Operating System:",
# self.os, "Memory:", self.memory)
#
#
# obj1 = laptop("intel CORE i7", "silver","Windows 11", "512 GB SSD")
# obj2 = laptop("intel CORE i5", "black","Windows 10", "1 TB HDD")

# class company using constructor and static variable, id, name, phone number, salary
# static variable are company name and location.

# class company:
#     company_name = "Wipro"
#     location_name = "Bangaluru"
#
#     def __init__(self, name, id, phone, salary):
#         self.name = name
#         self.id = id
#         self.phone = phone
#         self.salary = salary
#         print("Company:", company.company_name, "Location:", company.location_name, "Employee name:", self.name,
#               "Employee id:", self.id, "Phone number:", self.phone, "salary:", self.salary)
#
#
# obj1 = company("Thachu", 101, 9864738765, 10000)
# obj2 = company("Thacholi", 102, 8495763789, 100000)


# inheritance: The inheritance allows us to define a class that inheritance all the methods and properties from
# another class

# types of inheritance
# single
# multiple
# multi level
# hybrid
# hierarchical
