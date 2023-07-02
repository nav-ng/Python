# # # # # dictionary are used to store datas are key value pairs.
# # # # # a dictionary is collection which is ordered, changeable and do not allow duplicates.
# # # # syntax
# # # # dictionary={key1:value1,key2:value2}
# # #
# # #
person = {
    'name': 'Anziya',
    'age': '22',
    'phone': '3584269543',
}
# # # print(person)
# #
# #
# # how to access key in dictionary
# # in dictionary which is used to access keys:keys()
#
#
# x = person.keys()
# print(x)
#
# x1 = person.values()
# print(x1)
#
# person.update({'job': 'student'})
# print(person)
#
# person.update({'phone': '6835739856'})
# print(person)
#
# person['age'] = 22
# print(person)
#
# person.pop('age')
# print(person)
#
# # popitems:which is used to remove the last inserted item.
#
# person.popitem()
# print(person)
#
# # del keyword remove a specific keyword
# # del dict_name['key']
#
#
# del person['phone']
# print(person)
#
# # dictionary iteration:
# # for i in dictname:
# #     print(i)
#
#
# for i in person:
#     print(i)
# # #
# for i in person.values():
#     print(i)
# # #
# for i, j in person.items():
#     print(i, j)
#
#
# # items() method:it is a method which is used to return list of all dictionary keys with values
