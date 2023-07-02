print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSimple Calculator")
print("1.Addition\n2.Substration\n3.Multiplication\n4.Division")
choice = int(input("Enter your choice: "))
if choice in (1, 2, 3, 4):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if choice == 1:
        print(num1, '+', num2, '=', num1 + num2)
    elif choice == 2:
        print(num1, '-', num2, '=', num1 - num2)
    elif choice == 3:
        print(num1, 'x', num2, '=', num1 * num2)
    elif choice == 4:
        print(num1, '/', num2, '=', num1 / num2)
else:
    print("Invalid option")

