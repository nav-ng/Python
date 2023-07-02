row = int(input("Enter the number of row: "))
for i in range(1, row + 1):
    for j in range(1, row + 1 - i):
        print(end=" ")
    for j in range(row, -1, -1):
        print("*", end=" ")
    print()
