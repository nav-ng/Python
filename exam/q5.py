num = int(input("Enter a number: "))
temp = num
factorial = 1
while num > 0:
    factorial = factorial * num
    num -= 1
print("Factorial of", temp, "is", factorial)
