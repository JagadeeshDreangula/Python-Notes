################################# try and except #####################################

# try:
# name='jagadeesh'
# num=3
# add=name+num
# print(add)
# except:
#     add=name+str(num)
#     print(add)


# except:
#   print("An exception occurred")

##################################### Many Exceptions  #################################
# try:
    # print(x)
    # print(10/0)
# except NameError:
#   print("Variable x is not defined")
# except ZeroDivisionError:
#   print('Zero divisen error')
# except:
#   print("Something else went wrong")

####################################### else ##################################################
# try:
#   print('Hello')
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
###################################### finally #################################################
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

######################################### Raise ###################################################
# x = int(input('enter a number'))
# if x < 5:
#   raise Exception("Sorry, no numbers below zero")

x =1.2
if not type(x) is int:
  raise TypeError("Only integers are allowed")
