num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd  number: "))
num4 = int(input("Enter 4th number: "))
if num1 < num2 and num1 < num3 and num1 < num4:
    print(num1, "is the smallest number")
elif num2 < num3 and num2 < num4:
    print(num2, "is the smallest number")
elif num3 < num4:
    print(num3, "is the smallest number")
else:
    print(num4, "is the smallest number")
