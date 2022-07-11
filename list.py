# li=[]
# print(type(li))
# list=[10,'jagadeesh','python','python','python']
# print(list)
# tpl=(10,'jagadeesh','python','python','python')
# print(tpl)
# st={10,'jagadeesh','python','python','python'}
# print(st)
# dict={'one':1,'two':2,'three':3}
# print(dict['two'])
# li=[]#LIST
# tu=()#tuple
# se={}#set
# list1=[12,16,52,555]
# list2=[55,878,247]
# print(list1)
# print(list2)
# x="Learning Python is very very easy!!"
# l=x.split()
# print(l)
# print(type(l))
#
#
# mylist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(mylist)
#
list=[10,20,30,40,50]
#Remember that the first item has index 0.
txt='jagadeesh'
# print(len(list))
# print(len(txt))

# print(list[7])
# print(list[2])

#String, int and boolean data types:
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# n=[1,2,2,2,2,3,3,4,5]
# # print(n.count(1))
# print(n.count(7))
# n=[1,2,3,5,7]
# n.insert(3,4)
# print(n)
# n.insert(5,6)
# print(n)

# order1=["chicken","mutton","fish"]
# order2=["Rc","KFC","AFC"]
# order1.extend((1,2,3,4,5,6))
# print(order1)
# li2=['a','d','c','b']
# li.sort()
# print(li)
# print(li2)
# num=''
# for i in li:
#     num=i+num
# print(num)
# li.reverse()
# print(li[::-1])

# li.remove(3)
# li.clear()
# print(li.remove(3))

# print(n.index(2))
# print(n.index(2))
# print(n.index(3))
# print(n.count(3))
# print(n.count(4))
#
#
# #A list with strings, integers and boolean values
# list1 = ["abc", 34, True, 40, "male"]
# print(list1)
#
#
# #From Python's perspective, lists are defined as objects with the data type 'list':
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))
# li=[]
# a=('jagadeesh','likes','python')
# li=list(('jaga',1,10,'hellow'))
# print(li)
# print(type(li))
# #Using the list() constructor to make a List:
# thislist = list(("apple", "banana", "cherry"))   # note the double round-brackets
# print(thislist)
#
#
# #Print the second item of the list:
# list=["hai","welcome","python"]
# print(list[1])                             #The second item has index 1.
#
# #Print the first item of the list:
# list=["hai","welcome","python"]
# print(list[0])                             #The first item has index 0.
#
# #Print the third item of the list:
# list=["hai","welcome","python"]
# print(list[2])                             #The third item has index 2.
#
#
# #Print the last item of the list:
# list=["hai","welcome","python"]
# print(list[-1])
#
#With split() function:
# x='''"Learning Python is very very easy!!",\n
# "Learning Python is very very easy!!"'''
# l=x.split()
# print(l)
# print(type(l))
#
#with index:
# list=[10,20,30,40,50]       #Remember that the first item has index 0.
# print(list[0])
# print(list[5])
#
#with slice operator:
# n=[1,2,3,4,5,6,7,8,9]
# print(n[2:7:2])            #[start,stop,increment]
# print(n[0:5:1])            #Remember that the first item has index 0.
#
# #with len()
# n=[10,20,30,5,64,70,80,90]
# print(len(n))
#
#with count()
# n=[1,2,2,2,2,3,3,4,5]
# print(n.count(2))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))
#
#with index() function:
# n=[1,3,3,2]
# # print(n.index(1))
# print(n.index(2))
# print(n.index(3))
#
#
#with append() function:
# l=[]
# l.append(20)
# l.append('Python class')
# l.append('list data structure')
# print(l)
#
#
#with insert() function:
# n=[1,2,3,5,8,9]
# n.insert(3,454)#index,value
# print(n)
#
# #with extend() function:
# order1=["chicken","mutton","fish"]
# order2=["Rc","KFC","AFC"]
# order1.extend(order2)
# print(order1)
#
#with remove() function:
# a=[10,20,50,10,30]
# a.remove(10)
# a.remove(10)
# print(a)
#
# #with pop() function:
# n=[10,20,30,40]
# n.pop()   #you can index also for example print(n.pop(1)) like this. you cannot give index it will take last element.
# #                   #if the list is empty it will get errot for example n=[]
# print(n)
#
#
#with reverse() function:
# n=[11,12,15,18]
# n.reverse()
# print(n)
# name='jagadeesh'
# rev=''
# for i in name:
#     rev=i+rev
# print(rev)
#with sort() :
# n=[10,0,5,2,6,8]
# n.sort(reverse=True)
# print(n)

#Aliasing
# x=[10,20,30,40,50]
# y=x
# # print(y)
# y[1]=777
# print(y)
# print(x)
#
#By using slice operator:
# x=[10,20,30,40,50]
# y=x[:]
# # print(y)
# y[2]=789
# print(x)
# print(y)
#
#By using copy() function:
# x=[10,20,30,40,50]
# y=x.copy()
# # print(y)
# y[1]=585
# print(x)
# print(y)
#
#By concatenation operator (+):
# a=[10,20,30]
# b=[40,50,60]
# c=a+b
# print(c)
#
#By Repetition operator (*) :
# a=[55,85,96,36]
# b=a*3
# print(b)
#
#
#clear() function
# thislist=["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
#
#
#List comprehension:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[x  for x in fruits if "a" in x]
# print(newlist)
# l=[1,2,3,4,5,6,7,8]
# newlist=[f'{i} is  even'  if i%2==0 else f'{i} is odd' for i in l ]
# print(newlist)
# a,b=1,2
# b='my value is one {},{}'.format(a,b)
# print(b)
# li=[1,2.0,3.5,4,5,6,]
# # li as l
#
# li2=li
# li2.append(10)
# print(li)
# print(li2)
l=[1,2,3,4,5,6,7,8]
newlist=[]
for i in l:
    if i % 2 == 0:
        newlist.append(f'{i} is  even')
    else:
        newlist.append(f'{i} is odd')
print(newlist)

