# the hierarchical inheritance in which there is more than one inherited from a single parent


# class parent:
#     def f1(self):
#         body
#
#
# class child1(parent):
#     def f2(self):
#         body
#
#
# class child2(parent):
#     def f3(self):
#         body
#
#
# class child3(parent):
#     def f4(self):
#         body
#
#
# obj1 = child1()
# obj1.f1()
# obj1.f2()
# obj2 = child2()
# obj2.f1()
# obj2.f3()
# obj3 = child3()
# obj3.f1()
# obj3.f4()

# class details:
#     def data(self, name, salary, ):
#         self.name = name
#         self.salary = salary
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#
#
# class doctor(details):
#     def dfun(self, specialization, hospital_name):
#         self.spc = specialization
#         self.name = hospital_name
#         print("Specialization in:", self.spc)
#         print("Hospital name:", self.name)
#
#
# class engineer(details):
#     def efun(self, programing, company_name):
#         self.prgm = programing
#         self.name = company_name
#         print("Programing:", self.prgm)
#         print("Company name:", self.name)
#
#
# doc = doctor()
# doc.data("Amal", 10000)
# doc.dfun("General", "AIMS")
#
# eng = engineer()
# eng.data("Amal", 10000)
# eng.efun("C+", "TCS")


# class detailes:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#
#
# class doctor(detailes):
#     def __init__(self, name, salary, specialization, hospital_name):
#         super().__init__(name, salary)
#         self.spc = specialization
#         self.name = hospital_name
#         print("Specialization in:", self.spc)
#         print("Hospital name:", self.name)
#
#
# class engineer(detailes):
#     def __init__(self, name, salary, programing, company_name):
#         super().__init__(name, salary)
#         self.prgm = programing
#         self.name = company_name
#         print("Programing:", self.prgm)
#         print("Company name:", self.name)
#
#
# doc = doctor("Amal", 10000, "General", "AIMS", )
# eng = engineer("Sumal", 10000, "C+", "TCS")


# class detailes:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#
#
# class nurce(detailes):
#     def __init__(self, name, salary, department, hospital_name):
#         detailes.__init__(self, name, salary)
#         self.dept = department
#         self.h_name = hospital_name
#         print("Department:", self.dept)
#         print("Hospital:", self.h_name)
#
#
# class teacher(detailes):
#     def __init__(self, name, salary, subject, school):
#         detailes.__init__(self, name, salary)
#         self.subject = subject
#         self.school = school
#         print("Subject:", self.subject)
#         print("School:", self.school)
#
#
# nurce1 = nurce("Amala", 10000, "Ward", "MIMS")
# teacher1 = teacher("Vimala", 10000, "Maths", "NHSS VATTOLI")


