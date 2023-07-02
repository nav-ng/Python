from threading import *
import time

def square(num):
    print("Calculate square")
    for i in num:
        time.sleep(10)
        print("square=", i ** 2, current_thread().name)


def cube(num):
    print("Calculate cube")
    for i in num:
        time.sleep(10)
        print("Cube=", i ** 3, current_thread().name)


arr = [1, 2, 3, 4, 5]
square(arr)
cube(arr)

# what is thread, what is multi threading, what are the states associated with the thread, what is thread lifecycle, what
# is deadlock in thread, what is livelock, what is the difference b/w weight function and sleep function, what do you
# mean by a lightweight process and a heavyweight process, what is the difference b/w a multithreading and a
# multiprocessor.

# class Error(Exception):
#     pass
# class TooYoung(Error):
#     pass
# class TooOld(Error):
#     pass
#
# try:
#     num=int(input("Enter your age:"))
#     if num>=21 and num<=59:
#         print("You are eligible")
#     elif num<21:
#         raise TooYoung
#     elif num>59:
#         raise TooOld
# except TooYoung:
#     print("Too young for a vaccine")
#
# except TooOld:
#     print("too old for vaccine")
#
# except ValueError as e:
#     print(e)
# finally:
#     print("program completed..........")



