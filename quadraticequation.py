b = int(input("Enter the value of b: "))
a = int(input("Enter the value of a: "))
c = int(input("Enter the value of c: "))
d = ((b ** 2) - (4 * a * c)) ** 0.5
x1 = (-b + d) / 2 * a
x2 = (-b - d) / 2 * a
print("Solutions are ", x1)
print(x2)
