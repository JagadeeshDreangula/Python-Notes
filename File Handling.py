# f = open("jaga.txt",'r')
# print(f.read(5))
# f = open("demofile.txt", "rt")
# print(f)

###################################### read() method for reading the content of the file ##############################
# f = open("demofile.txt", "r")
# print(f.read())
####################################### Read Only some Characters ##############################################
# f = open("demofile.txt", "r")
# print(f.read(5))
####################################### Read Lines ##############################################
#
# f = open("demofile.txt", "r")
# print(f.read(2))
# ####################################### Loop through the file line by line ##############################################

# f = open("demofile.txt", "r")
# for x in f:
#   print(x)
########################################## Close Files ###############################################################
# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()
########################################  Write to an Existing File using"a"   ###########################################################
# f = open("jaga.txt", "a")  #"a" - Append
# f.write("Now the file has more content!")
# f.close()
# # #open and read the file after the appending:
# f = open("jaga.txt", "r")
# print(f.read())
########################################  Write to an Existing File using "w"  ###########################################################
# f = open("jaga.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# # print(f.read())
########################################  Create a New File   #########################################################
# f = open("myfile.txt", "x")
# f = open("myfile.txt", "w")
# f = open("myfile.txt", "a")
######################################## Delete a File  #######################################################
# f=open('python.txt','a')
# import os
# os.remove("python.txt")

########################################  Check if File exist   ###################################################
# import os
# if os.path.exists("python.txt"):
#   os.remove("python.txt")
# else:
#   print("The file does not exist")
######################################### Delete Folder ###########################################################
# import os
# os.rmdir("C:\Users\91810\Desktop\Python_class\day_14\hellow")
#You can only remove empty folders.
from bs4 import BeautifulSoup