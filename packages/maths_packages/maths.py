def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def fact(num):
    factorial = 1
    for i in range(num, 0, -1):
        factorial *= i
    return factorial


def revstring(string):
    return (string[::-1])