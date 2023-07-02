# it is used to change the behaviour of existing method and there is a need for at least two classes for method
# overriding. In method overriding inheritance is always required as it is done between parent class and child class

# class A:
#     def display(self):
#         print("Method A")
#
#
# class B(A):
#     def display(self):
#         print("Method B")
#
#
# obj = B()
# obj.display()
# here B overrides A.

# overriding using multiple inheritance

# class A:
#     def abc(self):
#         print("A")
#
#
# class B:
#     def abc(self):
#         print("B")
#
#
# class C(A, B):
#     def abc(self):
#         print("C")
#
#
# obj1 = C()
# obj1.abc()


# overriding using multilevel inheritance


# class A:
#     def abc(self):
#         print("A")
#
#
# class B(A):
#     def abc(self):
#         print("B")
#
#
# class C(B):
#     def abc(self):
#         print("C")
#
#
# obj1 = C()
# obj1.abc()
