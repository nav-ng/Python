# in python, it is defined as a process of handling complexity by hiding unnecessary information from the user. this
# is one of the core concept of object-oriented programing language.
# what is ABC in abstraction: This module that provides the infrastructure for defining abstract base classes.
# Python has a module called abc that offers the necessary tools for crafting an abstract base class.
# what is decorator(@abstractor method): Decorator can be extremely useful as they allow the extension of an existing
# function without any modification to the original function sourcecode.
# pass: it is a keyword which is used as a placeholder for future call. it is used when the user does not want any code
# to be executed.
from abc import ABC, abstractmethod


#
#
class parent(ABC):  # abstract class
    @abstractmethod
    def a(self):
        pass

    @abstractmethod
    def b(self):
        pass


class child1(parent):
    def a(self):
        print("child1 A")

    def b(self):
        print("Child1 B")

    def c(self):
        print("Child1 C")


obj1 = child1()
obj1.a()
obj1.b()
obj1.c()
