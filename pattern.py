limit = int(input("Enter the number of row: "))
for i in range(0, limit):
    for j in range(0, limit - i - 1):
        print(end=" ")
    for k in range(0, i+1):
        print("*", end=" ")
    print()