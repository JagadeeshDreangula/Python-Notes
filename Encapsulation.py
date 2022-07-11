# class Base:
#     def __init__(self):
#         # Protected member
#         self._a = 2
#
#
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling protected member of base class: ",self._a)
#
#         # Modify the protected variable:
#         self._a = 3
#         print("Calling modified protected member outside class: ", self._a)
# #
#
# # obj1 = Derived()
#
# #
# obj2 = Base()
# print(obj2.self._a)
#
# # Calling protected member
# # Can be accessed but should not be done due to convention
# print("Accessing protected member of obj1: ", obj1._a)
#
# # Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)
# #########################################################################################################################
class Base:
    def __init__(self):
        self.a = "Python"
        self.__c = "Jagadeesh"
        # print(self.__c)


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.a)
#
#
# # Driver code
obj=Derived()
# obj1 = Base()
# print(obj1.a)
#
# _a=2
# def _a():
