# class Person():
# #                                                         #normal class
#   def parent(self):
#       first_name='Jagadeesh'
#       last_name='Derangula'
#       print(first_name,last_name)
# #
# obj=Person()
# obj.parent()

##################################################### Single Inheritance ###########################################
class A(): #base class
    def parent(self):
        first_name ='Jagadeesh'
        last_name ='Derangula'
        print(first_name, last_name)
# # #
class B(A): #derived class or sub class
# # #
    def children(self):
        name='Ankitha'
        print(name)
# #
# #
# obj1=B()
# obj1.parent()
# obj1.children()
# names = Person2()
# names.parent()
# names.children()
############################################################### Multiple Inheritance #####################################
class A():
    def parent1(self):
        first_name ='Jagadeesh'
        last_name ='Derangula'
        print(first_name, last_name)
# #
class B():
    def parent2(self):
        first_name ='Eswari'
        last_name ='Batthala'
        print(first_name, last_name)
# #
class C(A,B):
#
    def children(self):
        name='Ankitha'
        name2='Arpitha'
        print(name)
# #
# #
# obj = C()
# obj.parent1()
# obj.parent2()
# obj.children()
###################################################################### MUlti Level Inheritance #############################################
class A():
    def parent(self):
        first_name ='gopal'
        last_name ='Derangula'
        print(first_name, last_name)
#
class B(A):
    def child(self):
            first_name = 'Jagadeesh'
            last_name = 'Derangula'
            print(first_name, last_name)
#
class C(B):
#
    def grand_child(self):
        name='Ankitha'
        print(name)

# obj = C()
# obj.parent()
# obj.child()
# obj.grand_child()
################################################################ Hierarchical Inheritance ################################
class A():
    def parent(self):
        first_name ='Jagadeesh'
        last_name ='Derangula'
        print(first_name, last_name)
#
class B():
    def child1(self):
        first_name ='Ankitha'
        print(first_name)

class C(A):
#
    def child2(self):
        name='Arpitha'
        print(name)
class D(B):
    def child3(self):
        print("HI")
class E(C,D):
    def hybrid(self):
        print('Hybrid seed')
#
obj = E()
obj.parent()
# obj.child2()
# # obj2=Person2()
# obj2.child1()
