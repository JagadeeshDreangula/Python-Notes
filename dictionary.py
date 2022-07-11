#Create and print a dictionary:
# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# print(thisdict)
num={'one':1,'two':2,'three':1}
# l=[1,2,3]
# print(l[0])
# print(num['two'])
# print(type(num))
# print(num)
#
# #Print the "brand" value of the dictionary:
car=	{"brand": "Ford","model": "Mustang","year": 1964}
# print(car["year"])
#
# #Duplicate values will overwrite existing values:
# thisdict = {"brand": "Ford","model": "Mustang","year": 1964,"year": 2020}
# print(thisdict)
#
#
car = {"brand": "Ford","model": "Mustang","year": 1964}
# print(car)

x = car.keys()
#
# print(x) #before the change
#
# car["color"] = 4
# print(car)
#
# print(x) #after the change
#
# #items()
car = {"brand": "Ford","model": "Mustang","year": 1964}
#
x = car.items()
#
# print(x) #before the change
#
car["year"] = 2020
#
# print(x) #after the change
# print(car)

#Checking if key exists

# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")
#
#
# d={100:"apple",200:"cherry",300:"sapota"}
# print(d)
# d[300]="jagadeesh"
# print(d)
# d[100]="Bhaskar"
# print(d)
# dict={100:"apple",200:"cherry",300:"sapota"}
# print(dict)
# dict.update({700:"Kiwi",600:'mango'})
# print(dict)
# dict={100:"apple",200:"cherry",300:"sapota"}
# dict.pop(300)
# print(dict)
# dict={100:"apple",200:"cherry",300:"sapota"}
# del dict[100]
# print(dict)


#
# dict={100:"apple",200:"cherry",300:"sapota"}
# dict[500]="mango"
# print(dict)
#
# dict={100:"apple",200:"cherry",300:"sapota"}
# dict.pop(200)
# print(dict)
#
# dict={100:"apple",200:"cherry",300:"sapota"}
# dict.clear()
# print(dict)

# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# for x in thisdict:
#   print(thisdict[x])


# car =	{"brand": "Ford","model": "Mustang","year": 1964}
# for x in car:
#   print(car[x])  ##To print values

# thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
# for x, y in thisdict.items():
#     print(x,y)

# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# # x=thisdict
x = thisdict.copy()
print(x)
# x[1]='first'
# print(x)
# print(thisdict)
#
# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# mydict=dict(thisdict)
# print(mydict)






