start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
sum=0
for i in range(start, end):
    if i % 2 == 0:
        print(i)
        sum = sum + i
print("The sum is", sum)
