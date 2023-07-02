factorial = 1
num = int(input("Enter a number: "))
temp = num
while num > 0:
    factorial *= num
    num -= 1
print("The factorial of", temp, "is", factorial)
