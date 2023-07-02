# it is in which a single child class that can inherit from more than one parent class.

# syntax
# class parent1:
#     def f1(self):
#         print
# class parent2:
#     def f2(self):
#         body
# class child(parent1,parent2):
#     def f3(self):
#         body
# obj1=child()
# obj.f1()
# obj.f2()


# class parent1:
#     def f1(self):
#         print("Hello")
#
#
# class parent2:
#     def f2(self):
#         print("chichu")
#
#
# class child(parent1, parent2):
#     def f3(self):
#         print("good bye")
#
#
# obj1 = child()
# obj1.f1()
# obj1.f2()
# obj1.f3()


# class company:
#     def function1(self, company_name):
#         self.name = company_name
#         print("company name:", self.name)
#
#
# class teamleader:
#     def function2(self, leader_name, department):
#         self.name = leader_name
#         self.dept = department
#         print("Leader name:", self.name)
#         print("Department:", self.dept)
#
#
# class employee(company, teamleader):
#     def function3(self, employee_name, salary):
#         self.name = employee_name
#         self.salary = salary
#         print("Employee name:", self.name)
#         print("Salary:", self.salary)
#
#
# obj1 = employee()
# obj1.function1("Fruit bae")
# obj1.function2("Manthappan", "Food testing")
# obj1.function3("nandhu", 10000)

# class company:
#     def __init__(self, company_name):
#         self.name = company_name
#         print("Company name:", self.name)
#
#
# class teamleader:
#     def __init__(self, leader_name, department):
#         self.name = leader_name
#         self.dept = department
#         print("Leader name:", self.name)
#         print("Department:", self.dept)
#
#
# class employee(company, teamleader):
#     def __init__(self, company_name, leader_name, department, employee_name, salary):
#         company.__init__(self, company_name)
#         teamleader.__init__(self, leader_name, department)
#         self.name = employee_name
#         self.salary = salary
#         print("Employee name:",self.name)
#         print("salary:",self.salary)
#
#
# obj1 = employee("Njam Njam foods", "Manthu", "food clearing", "nandhu", 1000)
