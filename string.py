# txt = "banana is my favorite fruit."
# print(txt.title())
txt = "Hello Jaga!"
# print(txt.zfill(20))
# mytable = txt.maketrans("g", "y")
# # print(mytable)
# print(txt.translate(mytable))
# print("PYTHON is A programming {} {} {} language".format(num,val2,val1))
# point = {'x':4,'y':-5}
# print('{x} {y}'.format(**point))
# print(type(b))
# n=1
# print(type(n))
# m='1'
# print(type(m))



# print(name.isupper())

''' istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string(txt = "banana" x = txt.ljust(20) print(x, "is my favorite fruit."))
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations(The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.)
                [txt = "Hello Jaga!"
                mytable = txt.maketrans("g", "y")
                print(mytable)#use a dictionary with ascii codes to replace 103 (g) with 121 (y):            
                print(txt.translate(mytable))]
translate()	    Returns a translated string   
partition()	    Returns a tuple where the string is parted into three parts[text = "I could eat bananas all day"x = text.partition("bananas")print(x)]
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list[langs = 'C,Python,R,Java,SQL,Hadoop'print(langs.rsplit(',', 3))]
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list[str = "this is \nstring example....\nwow!!!"print (str.splitlines( ))]
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
upper()	        Converts a string into upper case
zfill()	        Fill with 0[a = "hello" b = "welcome to the jungle"c = "10.000"print(a.zfill(10))print(b.zfill(10))print(c.zfill(10))]'''
########################################################################################################################################
'''common errors'''
# s='this is single"quote symbol'
# print(s)
# s='this is single\'quote symbol'
# print(s)
# s="this is single'quote symbol"
# print(s)
# s='this is double"quote symbol'

# s="this is double\"quote symbol"
# print(s)
# s='The\"python notes"\by \'jagadeesh\''
# print(s)
# s='The"python notes"by \'jagadeesh\''
#######################################################################################
'''How to access characters of String
1)By using index
2)By using sliceoperator'''
str_text='Python'
# temp=''
# for txt in str_text:
#     # print(txt)
#     temp=txt+temp
# print(temp)
# print(str_text[::-1])

# print(str_text[0])
# print(str_text[0:10:3])
# print(n[3])#index
# print(n[8])
# print(str_text[:5])
# print(n[0:5:3])#not consider last number
# n='pythonsmdl'
# print(n[4::-2])
# m=n.reverse()
# print(m)
####################################################################
"""Mathematical operators for string
1) + operator for concatenation
2) *operator for repetion"""
# print('jagadeesh'+str(1))#concatenation possible  b/w strings only
# print('python'*2)
#####################
'''checking membership'''
n='python'
print('t'in n)#in
print('t'not in n)#not in
#####################################
'''Note: String the most commonly used Data type in any project and in any programming language.
         so we should aware complete information about string data type'''
# import glob
# print(glob.glob())