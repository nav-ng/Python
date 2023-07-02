# it is the combination of hierarchical inheritance and multiple inheritance.
# class parent:
#     def f1(self):
#         print("Hello")
#
#
# class child1(parent):
#     def f2(self):
#         print("Hello1")
#
#
# class child2(parent):
#     def f3(self):
#         print("Hello2")
#
#
# class child3(child1, child2):
#     def f4(self):
#         print("Hello3")
#
#
# obj = child3()
# obj.f1()
# obj.f2()
# obj.f3()
# obj.f4()


# class university:
#     def f1(self, u_name, u_location):
#         self.name = u_name
#         self.location = u_location
#         print("University:", self.name)
#         print("Location:", self.location)
#
#
# class college(university):
#     def f2(self, college_name):
#         self.name = college_name
#         print("College:", self.name)
#
#
# class cource(university):
#     def f3(self, cource_name):
#         self.name = cource_name
#         print("Cource:", self.name)
#
#
# class student(college, cource):
#     def f4(self, r_no, s_name):
#         self.no = r_no
#         self.name = s_name
#         print("Roll no:", self.no)
#         print("Name:", self.name)
#
#
# obj1 = student()
# obj1.f1("KTU", "Kollam")
# obj1.f2("TKM")
# obj1.f3("CSE")
# obj1.f4(35, "Naveen")

# using constructor

class university:
    def __init__(self, u_name, u_location):
        self.name = u_name
        self.lctn = u_location
        print("University:", self.name)
        print("Location:", self.lctn)


class college(university):
    def __init__(self, u_name, u_location, clg_name):
        university.__init__(self, u_name, u_location)
        self.name = clg_name
        print("College:", self.name)


class course(university):
    def __init__(self, course_name):
        self.name = course_name
        print("Course:", self.name)


class student(college, course):
    def __init__(self, u_name, u_location, clg_name, course_name, r_no, s_name):
        college.__init__(self, u_name, u_location, clg_name)
        course.__init__(self, course_name)
        self.no = r_no
        self.name = s_name
        print("Roll no:", self.no)
        print("Name:", self.name)


obj1 = student("KTU", "Trivandrum", "TKM", "B-tec", 35, "Naveen")
