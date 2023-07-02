num = int(input("Enter a number: "))
temp = num
armstrong = 0
while num > 0:
    rem = num % 10
    armstrong += rem ** 3
    num //= 10
if armstrong == temp:
    print("The number is armstrong")
else:
    print("The number is not an armstrong")
