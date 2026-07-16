class Account:
    def __init__(self, accno, pwd):
        self.accno=accno
        self.__pwd=pwd #private attribute

    def reset(self):
        print(self.__pwd)

a1=Account(12263738, "abcdf")
print(a1.accno)
# print(a1.pwd) #bad practice so use private attribute
#print(a1.__pwd) #can't access private attribute directly from outside the class
a1.reset() #can acess priv attribute from class method

class Person:
    __name="Anonymous"

    def __hello(selfp):
        print("Hello user!!")

    def welcome(self):
        self.__hello()

p1=Person()
# print(p1.__name) #error
# print(p1.__hello()) #error
p1.welcome()
 