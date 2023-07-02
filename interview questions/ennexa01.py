# def first_digit(digit):
#     once = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
#             10: "Ten",
#             11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
#             18: "Eighteen", 19: "Nineteen"}
#     for i in once.keys():
#         if digit == i:
#             ans = once[i]
#             return str(ans)
#
#
# def second_digit(digit):
#     tens = {0: "", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
#     for i in tens.keys():
#         if digit == i:
#             ans = tens[i]
#             return str(ans)
#
#
# def getvalue(num):
#     value = []
#     while num > 0:
#         value.append(num % 10)
#         num //= 10
#     return value
#
#
# def num_to_word(num):
#     if num < 20:
#         return first_digit(num)
#     elif 19 < num < 100:
#         value = getvalue(num)
#         return second_digit(value[1]) + " " + first_digit(value[0])
#     elif 99 < num < 1000:
#         value = getvalue(num)
#         return first_digit(value[2]) + " Hundred " + second_digit(value[1]) + " " + first_digit(value[0])
#     elif 999 < num < 10000:
#         value = getvalue(num)
#         print(value)
#         return first_digit(value[3]) + " Thousand " + first_digit(value[2]) + " Hundred " + second_digit(
#             value[1]) + " " + first_digit(value[0])
#
#
# print(num_to_word(972))


# def num_to_word(num):
#     once = {
#         0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
#         10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
#         17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
#     }
#
#     tens = {
#         2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
#     }
#
#     if num < 20:
#         return once[num]
#     elif num < 100:
#         return tens[num // 10] + " " + once[num % 10]
#     elif num < 1000:
#         return once[num // 100] + " Hundred " + num_to_word(num % 100)
#     elif num < 10000:
#         return once[num // 1000] + " Thousand " + num_to_word(num % 1000)
#
#
# print(num_to_word(2403))
