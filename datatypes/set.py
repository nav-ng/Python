# # set:unordered collection of data types. it is iterable and has no duplicate values.
#
# represent using curly bracket. set is un indexed.


s1 = {"a", "b", "c"}
# print(s1)
#
# print(len(s1))
#
# for i in s1:
#     print(i)
#
# s1.add("q")
# print(s1)

# update() method it is used to add items from another set


s2 = {"1", "3", "5"}
s1.update(s2)
print(s1)
#
s3 = [7, 9, 0]
s1.update(s3)
print(s1)
#
s4 = (12, 45, 63, "3")
s1.update(s4)
print(s1)

# #remove()to remove items from a set
# s2.remove("1")
# print(s2)

# s2.discard("2")
#
# s2.pop()
# print(s2)

# intersection_update method: it is used to keep only items that are present in both set


# s2.intersection_update(s4)
# print(s2)

# symmetric_difference_update():
# method will keep only the elements that ae not present  in both set.


# s2.symmetric_difference_update(s4)
# print(s2)

# what is the difference between a set and a frozen set: frozen set is an inbuilt function in python which takes an
# iterable object as input and makes the immutable,simply it freeze iterable object and makes them unchangeable

# list1 = [1, 2, 3]
# list2 = frozenset(list1)
# list2.append(2)
# print(list2)
