i = 100
oddsum = 0
evensum = 0
while i <= 200:
    if i % 2 == 0:
        evensum += i
    else:
        oddsum += i
    i += 1
print("The sum of even numbers between 100 and 200= ", evensum)
print("The sum of odd numbers between 100 and 200= ", oddsum)
