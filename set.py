l = ["apple", "banana", "cherry", "apple"]
# print(l)
t = ("apple", "banana", "cherry", "apple")
# print(t)
# s = {"apple", "banana", "cherry", "apple"}
# print(s)
# s.add("orange")
# print(s)
s = {"apple", "banana", "cherry"}
s2= {"pineapple", "mango", "papaya"}
s.update({"pineapple", "mango"})
# print(s)
# mylist = ("kiwi", "orange")
# s.update(mylist)
# print(s)
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)
#
# #join two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2,3}
set3 = set1.union(set2)
print(set3)
#
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)
#
# x = {"apple", "banana", "cherry",'google'}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)
#
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
y.symmetric_difference_update(x)
# print(y)
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)
