cost = int(input("Enter the cost of bike: "))
if cost > 100000:
    tax = (cost * 15) / 100
    print("The tax you have to pay is", tax)
elif 50000 < cost <= 100000:
    tax = (cost * 10) / 100
    print("The tax you have to pay is", tax)
else:
    tax = (cost * 5) / 100
    print("The tax you have to pay is", tax)
