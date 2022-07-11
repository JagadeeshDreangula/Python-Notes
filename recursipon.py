# import sys
# # print(sys.getrecursionlimit())
# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())
# def rec():
#   print('hellow')
#   rec()
# rec()
############################################
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     return result
#   else:
#     result = 0
#     return result
#
# print("\n\nRecursion Example Results")
# result=tri_recursion(4)
# print(result)
#################################################################################
# 4!=4*3*2*1*0
# 0!=1
# 4!=1*2*3*4
#finding Factorial
# n=3
# fact=1
# for i in range(1,n+1):
#    fact=fact*i
# print(f'factorial of{n}! is', fact)
####################################################################
# def fact(n): #5!
#   f=1
#   for i in range(1, n + 1):
#     f = f * i
#   print(f'factorial of {n}! is', f)
# #
# fact(5)
#########################################################################
# def fact(n):            #recursion
#   if (n == 0):
#     return 1
#   return n *fact(n - 1) #5!==5*4!
# #
# print("\nFactorial value")
# result=fact(2)
# print(result)

