# a multilevel inheritance in which a class is derived from one class which is already derived from another class.
# syntax
# class parent:
#     def f1(self):
#         body
# class derived1(parent):
#     def f2(self):
#         body
# class derived2(derived1):
#     def f3(self):
#         body
# obj1=derived2()
# obj1.f1()
# obj1.f2()
# obj1.f3()

# class grandfather:
#     def f1(self, grandfather_name):
#         self.name = grandfather_name
#         print("Grandfather name:", self.name)
#
#
# class father(grandfather):
#     def f2(self, father_name):
#         self.name = father_name
#         print("Father name:", self.name)
#
#
# class son(father):
#     def f3(self, son_name):
#         self.name = son_name
#         print("Son name:", self.name)
#
#
# obj1 = son()
# obj1.f1("Yedukula koppa nagaraj reddy")
# obj1.f2("Nagaraga raddy")
# obj1.f3("Reddy")


# class grandfather:
#     def __init__(self, gname):
#         self.name = gname
#         print("Grandfather name:", self.name)
#
#
# class father(grandfather):
#     def __init__(self, gname, fname):
#         grandfather.__init__(self, gname)
#         self.name = fname
#         print("Father name:", self.name)
#
#
# class son(father):
#     def __init__(self, gname, fname, sname):
#         father.__init__(self, gname, fname)
#         self.name = sname
#         print("son name:", self.name)
#
#
# obj1 = son("gname", "fname", "sname")
