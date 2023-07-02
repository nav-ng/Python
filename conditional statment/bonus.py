salary = int(input("Enter your salary: "))
year = int(input("Enter your service period: "))
if year > 10:
    bonus = (salary * 10) / 100
    print("The bonus is", bonus)
elif 6 <= year <= 10:
    bonus = (salary * 8) / 100
    print("The bonus is", bonus)
else:
    bonus = (salary * 5) / 100
    print("The bonus is", bonus)
