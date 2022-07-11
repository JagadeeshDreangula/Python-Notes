# from abc import ABC, abstractmethod
# #
# class Polygon(ABC):
# #
#     @abstractmethod
#     def no_of_sides(self):
#       None
# #
# class Triangle(Polygon):
# #
#     def no_of_sides(self):              # overriding abstract method
#         print("I have 3 sides")
# #
# class Quadrilateral(Polygon):
# #
#     def no_of_sides(self):          # overriding abstract method
#         print("I have 4 sides")
#
# #
# class Pentagon(Polygon):
# #
#     def no_of_sides(self):            # overriding abstract method
#         print("I have 5 sides")
#
# class Hexagon(Polygon):
#
#     def no_of_sides(self):           # overriding abstract method
#         print("I have 6 sides")
# #
# #
# #
# #
# # # Driver code
# R = Triangle()
# R.no_of_sides()
# #
# K = Quadrilateral()
# K.no_of_sides()
# #
# # R = Pentagon()
# # R.no_of_sides()
# #
# K = Hexagon()
# K.no_of_sides()

################################################################################################################################
import abc
from abc import ABC, abstractmethod


class R(ABC):
    def rk(self):
        print("Abstract Base Class")


class K(R):
    def rk(self):
        super().rk()
        # print("subclass ")


# Driver code
r = K()
r.rk()