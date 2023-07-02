# findall()
# the method returns a list containing all the matches
import re
str="my first number is 12345 and second number is 09876. that's all"
# match=input("Enter string to be searched: ")
# print(re.findall(match,str))

# pattern='\D+'
# print(re.findall(pattern,str))

# match=input("Enter word to be searched: ")
# x= re.search(match, str)
# if x:
#     print("Yes, we have a match")
# else:
#     print("No match found")

# txt1="Arun and Arjun are students"
# print(re.split('\s',txt1,2))
# print(re.sub("Arun", "Amal", txt1))
# txt2="Luminar located in Kakkanad"
# print(re.sub('\s', '#', txt2, 2))

# fullmatch method returns a match object if the pattern matches the whole string
# write a regex pattern to validate a name
# rule="[A-Za-z]+"
# nm=input("Enter name: ")
# x=re.fullmatch(rule,nm)
# if x:
#     print("ok")
# else:
#     print("shit")

# write a regex rule to validate a name that ranges b/w 5 and 10
# stars with uppercase and others are lower case letter and min 5 and max 15

rule="^[A-Z][a-z]{4-14}"
