startingnumber = int(input("Enter starting number: "))
endingnumber = int(input("Enter ending number: "))
for i in range(startingnumber, endingnumber):
    if i % 2 == 0:
        print(i)
