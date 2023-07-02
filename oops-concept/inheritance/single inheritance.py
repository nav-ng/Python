# it is an inheritance method that enables a derived class/child class to inheritance the properties from the single
# parent class.


# class A-base class(parent class)
# class B-derived class(child class)

# syntax
# class parent:
#   def function1(self):
#       body
# class child(parent):
#   def function2(self):
#       body
# obj1=child()
# obj1.function1()
# obj1.function2()


# single inheritance using arguments


# class company:
#     def setval1(self, company_name, location):
#         self.name = company_name
#         self.lct = location
#         print("Company name:", self.name)
#         print("Location:", self.lct)
#
#
# class employee(company):
#     def setval2(self, employee_name, salary):
#         self.emp_name = employee_name
#         self.salary = salary
#         print("Employee name:", self.emp_name)
#         print("salary:", self.salary)
#
#
# obj1 = employee()
# obj1.setval1("TCS", "LONDON")
# obj1.setval2("AMAL", 10000)


# create  single inheritance program using args


# class college:
#     def value1(self, college_name, location):
#         self.name = college_name
#         self.lct = location
#         print("College name:", self.name)
#         print("Location:", self.lct)
#
#
# class student(college):
#     def value2(self, student_name, department):
#         self.name = student_name
#         self.dept = department
#         print("Student name:", self.name)
#         print("Department name:", self.dept)
#
#
# obj1 = student()
# obj1.value1("CEK", "Kidangoor")
# obj1.value2("Naveen", "CSE")


# single inheritance using constructor


# class company:
#     def __init__(self, company_name, location):
#         self.name = company_name
#         self.lct = location
#         print("Company name:", self.name)
#         print("Location:", self.lct)
#
#
# class employee(company):
#     def __init__(self, company_name, location, employee_name, salary):
#         super().__init__(company_name, location)
#         self.emp_name = employee_name
#         self.salary = salary
#         print("Employee name:", self.emp_name)
#         print("salary:", self.salary)
#
#
# obj1 = employee("TCS", "LONDON", "Gaylen", 10000)

# super(): this method which is used to give access to the methods and properties of a parent or sibling class(only
# for one parent cases)

# class college:
#     def __init__(self, college_name, location):
#         self.name = college_name
#         self.lct = location
#         print("College name:", self.name)
#         print("Location:", self.lct)
#
#
# class student(college):
#     def __init__(self, college_name, location, student_name, department):
#         super().__init__(college_name, location)
#         self.name = student_name
#         self.dept = department
#         print("Student name:", self.name)
#         print("Department name:", self.dept)
#
#
# obj1 = student("CEK", "Kidangoor", "Mukhil", "CSE")

# create a single inheritance program using constructor and arg
