#single inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car): #inherits properties of parent class:Car
    def  __init__(self, name):
        self.name=name

c1=ToyotaCar("fortuner")
print(c1.name)
c1.start()
    
c2=ToyotaCar("prius")
print(c2.name)
print(c2.color)

#multi-level inheritance
class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand=brand

class Fortuner(ToyotaCar): #inherits properties of ToyotaCar as well as Car
    def __init__(self, type):
        self.type=type

c1=Fortuner("diesel")
c1.start()

# multiple inheritance
class A:
    varA = "Welcome to A World"

class B:
    varB = "Welcome to B World"

class C(A,B):
    varC = "Welcome to C World"

p1=C()
print(p1.varC)
print(p1.varB)
print(p1.varA)

