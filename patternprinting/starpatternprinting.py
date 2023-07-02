#  a = ["a", "b", "c"]
#  b = ["c", "d", "e"]
#  for i in a:
#      for j in b:
#          print(i, j)


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)
#     print()

#  limit=int(input("Enter the number of rows: "))
#  for i in range(limit):
#      for j in range(i+1):
#          print("*", end=(' '))
#      print()
#

# limit = int(input("Enter the number of rows: "))
# for i in range(limit):
#     for j in range(limit - i):
#         print("*", end=" ")
#     print()

# size = int(input("Enter row size: "))
# for i in range(size):
#     for j in range(size):
#         print('*', end=" ")
#     print()

# size = int(input("Enter row size: "))
# for i in range(size):
#     for j in range(size - i - 1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("*", end=" ")
#     print()

# size = int(input("Enter the row size: "))
# for i in range(size):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(size - i):
#         print("*", end=" ")
#     print()

# size = int(input("Enter number of items in starting and ending row: "))
# for i in range(size):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(size - i):
#         print("*", end=" ")
#     print()
# for i in range(size):
#     for j in range(size - i - 1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("*", end=" ")
#     print()


# size = int(input("Enter increment limit: "))
# for i in range(size-1):
#     for j in range(size - i - 1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("*", end=" ")
#     print()
# for i in range(size):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(size - i):
#         print("*", end=" ")
#     print()


# size = int(input("Enter increment limit: "))
# for i in range(size):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()
# for i in range(size - 1):
#     for j in range(size - i - 1):
#         print("*", end=" ")
#     print()

# height = int(input("Enter the height: "))
# for i in range(height):
#     if i < height - 1:
#         for j in range(1, 2 * height):
#             if j == height - i or j == height + i:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#     else:
#         for k in range(1, 2 * height):
#             if i == height - 1:
#                 print("*", end="")
#     print()


# size = int(input("Enter an odd row size: "))
# x = int(size // 2)
# for i in range(x):
#     for j in range(x - i):
#         print(" ", end="")
#     for k in range(1):
#         print("*", end="")
#     print()
# print("* * * * *")
# for i in range(x):
#     for j in range(i + 1):
#         print(" ", end="")
#     for k in range(1):
#         print("*", end="")
#     print()


# size = int(input("Enter odd row size: "))
# for i in range(size):
#     for j in range(size):
#         if j == i or j == size - 1 - i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# size = int(input("Enter the row size: "))
# for i in range(size):
#     for j in range(i):
#         if j == 0 or j == i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#     if i == size - 1:
#         for k in range(size):
#             print("*", end="")

# size = int(input("Enter side measurement of square: "))
# for i in range(size):
#     if i == 0 or i == size - 1:
#         for j in range(size):
#             print("*", end=" ")
#     else:
#         for j in range(size):
#             if j == 0 or j == size - 1:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#     print()


# limit = int(input("Enter limit of incrementing row: "))
# for i in range(1, limit + 1):
#     for j in range(limit - i):
#         print(" ", end=" ")
#     for k in range((2 * i - 1)):
#         print("*", end=" ")
#     print()
# for i in range(limit, 1, -1):
#     for j in range(limit - i + 1):
#         print(" ", end=" ")
#     for k in range(2 * i - 3):
#         print("*", end=" ")
#     print()





