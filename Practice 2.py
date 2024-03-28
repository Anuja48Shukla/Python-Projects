# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)
#
# for i in range(len(thistuple)):
#     print(thistuple[i])
#
# thistuple_new = thistuple*2
# print(thistuple)
#
# t = thistuple_new.count("apple")
# print(t)
from typing import Set
#
# set1 = {13, "abc", True, 25.7}
# print(dir(set))
#
# set2 = {"apple", "banana", "cherry", True, 1, 2}
# print(set2)

dict3 = dict(Name="Raj", Age=34, Country= "USA")
print(dict3)

# print(dict3["Age"])
# x = dict3.get("Country")
# print(x)
#
# keyslist = dict3.keys()
# print(keyslist)
#
# dict3["Salary"] = 1000000
# #keyslist = dict3.keys()
# print(keyslist)
# print(dict3)
#
# dictvalues = dict3.values()
# print(dictvalues)
#
# dict3["Name"] = "Ravi"
# print(dict3)
#
# items = dict3.items()
# print(items)
# print(type(items))

if "Age" in dict3:
    print("exists")

dict3.update({"Bonus" : 65000})
print(dict3)

dd = {"Acc" : 12345}
dict3.update(dd)
print(dict3)

dict3.popitem()
print(dict3)

del dict3["Country"]
print(dict3)

for x,y in dict3.items():
    print(x,y)

dict_new = dict(dict3)
print(dict_new)






