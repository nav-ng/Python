# stack: it is a linear data structure that consisting of a set of homogeneous elements.
# it is based on the principle of last in first out (LIFO).
# two major operation, namely push and pop.
# the push operation adds an element to the stack.
# pop operation remove an element from the top position.
# the stack concept is used in programing  and memory organization in computers.
# list/array
# queue: A queue is a linear structure which follows a particular order in which the operation are performed.
# the order is first in first out.
# two major operations, namely enqueue and dequeue.
# enqueue: insert into a queue.
# dequeue: delete from queue.
# stack program
# stk = []  # empty stack
# size = int(input('enter the size of stack: '))  # 2
# top = 0
# def push():
#     global top, size
#     if top >= size:  # 0>=2
#         print("stack is full")
#     else:  # true
#         p = int(input("enter the element to insert: "))  # 1
#         stk.append(p)  # [1]
#         top += 1  # top=1
#         print(stk)  # [1]
#
#
# def pop():
#     global top, size
#     if top <= 0:  # 1<=0
#         print("stack is empty")
#     else:  # true
#         stk.pop()  # []
#         top -= 1  # top=0
#         print(stk)  # []
#
#
# while True:
#     print('operation to perform')
#     option = int(input('1.PUSH\t\t2.POP\n'))
#     if option == 1:
#         push()
#     elif option == 2:
#         pop()
#     else:
#         print("invalid input....")

# queue program

# q = []  # []
# size = int(input("enter the size of queue: "))  #
# top = 0
#
#
# def enqueue():
#     global top, size  # rear=0 front=0 size=3
#     if top >= size:  # 1>=2
#         print('queue is full')
#     else:
#         p = int(input("enter the element to insert: "))  # 2
#         q.insert(top, p)  # insert(position, element)
#         top += 1  # top=2
#         print(q)  # [1 ,2 ]
#
#
# def dequeue():
#     global top, size
#     if top == 0:  # 1==0 0==0
#         print('queue is empty')
#     else:
#         q.pop(0)  # []
#         top -= 1  # 0
#         print(q)  # []
#
#
# while True:
#     print('enter the option\n')
#     option = int(input("1.ENQUEUE \t\t 2.DEQUEUE"))
#     if option == 1:
#         enqueue()
#     elif option == 2:
#         dequeue()
#     else:
#         print("invalid input.....")


# modules and packages:
# collections of functions / set of functions
# with .py extension

# 1.build-in module:
# math module
# calendar module
# time module
# os module
# datetime module
# random module

# 2.user defined modul


# q = []
#
# size = int(input("Enter the size of queue: "))
# top = 0
#
#
# def enqueue():
#     global top, size
#     if top >= size:
#         print("The queue is full")
#     else:
#         num = int(input("Enter element to be insert: "))
#         q.append(num)
#         top += 1
#         print(q)
#
#
# def dequeue():
#     global top, size
#     if top == 0:
#         print("Queue is empty")
#     else:
#         q.pop()
#         top -= 1
#         print(q)
#
#
# while True:
#     print("Operation to be performed: ")
#     option = int(input("1.enqueue\t2.dequeue\n"))
#     if option == 1:
#         enqueue()
#     else:
#         dequeue()




