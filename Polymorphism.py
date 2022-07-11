# name='jagadeesh'
# last_name='Derangula'
n=1
m=2
# li=[1,2,3,4,5,6]
# print(len(li))
# print(len(name))
# print(name+last_name)
# print(n+m)



########################################## Method overriding ########################################
class Bird:
    def intro(self):
        print("There are different types of birds")

    def flight(self):
        print("Most of the birds can fly but some cannot")
#
#
class Parrot(Bird):
    def bird(self):
        print('parrot')
    # def flight(self):
    #     print("Parrots can fly")
#
#
class Penguin(Bird):
    def flight(self):
        print("Penguins do not fly")
#
#
obj_bird = Bird()
obj_parr = Parrot()
obj_peng = Penguin()

# obj_bird.intro()
# obj_bird.flight()
#
# obj_parr.intro()
obj_parr.flight()

# obj_peng.intro()
# obj_peng.flight()
# obj_bird.flight()


################################################# method over loading #######################################################
# def add(a=None,b=None,c=None,d=None):
#     print(a,b,c,d)
# add(1,2,3,4)
# add(1,2)
# add('hellow','hi','how','r u')
# add(1,2,3)
# a=1
# print(a)
# a=2
# print(a)
# a=3
# print(a)
# a=4
# print(a)
