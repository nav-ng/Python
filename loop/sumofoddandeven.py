evensum = 0
oddsum = 0
for i in range(1, 51):
    if i % 2 == 0:
        evensum += i
    else:
        oddsum += i
print("The sum of odd numbers= ", oddsum)
print("The sum of even numbers= ", evensum)
