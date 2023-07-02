percentage = int(input("Enter your mark percentage: "))
if 81 <= percentage <= 100:
    print("your grade is A+")
elif 71 <= percentage <= 80:
    print("Your grade is A")
elif 61 <= percentage <= 70:
    print("Your grade is B+")
elif 51 <= percentage <= 60:
    print("Your f=grade is B")
elif 41 <= percentage <= 50:
    print("Your grade is C+")
elif 31 <= percentage <= 40:
    print("Your grade is C")
else:
    print("You are failed")
