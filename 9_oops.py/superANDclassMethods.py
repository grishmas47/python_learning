#super method: used to access methods of parent class
class Car:
    def __init__(self, type):
        self.type=type

    @staticmethod
    def start():
        print("car has started...")

    @staticmethod
    def stop():
        print("car has stopped...")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name=name
        super().__init__(type) #parent class ko bhitra constructor call huncha ra tesbhitra ko type
        super().start()

c1=ToyotaCar("fortuner", "diesel") #first of init constructor is called
print(c1.name)
# c1.start()
print(c1.type)

# class method
class Person:
    name="anonymous" #class attribute

    def changeName(self, name):
        self.name=name #creates a new name but doesn't change the class name/attribute

p1=Person()
p1.changeName("himal")
print(p1.name)
print(Person.name)

#1
class Person:
    name="anonymous"

    def changeName(self, name):
        Person.name=name #changes the class attribute directly

p1=Person()
p1.changeName("himal")
print(p1.name)
print(Person.name)

#2
class Person:
    name="anonymous"

    def changeName(self, name):
        self.__class__.name="Kumar" #hard coded

p1=Person()
p1.changeName("himal")
print(p1.name)
print(Person.name)

#3 Function ko bhitra class lai directly access garne=class methods
class Person: #proper way to use class method
    name="anonymous"

    @classmethod #decorator takes this function and returns a new and better function that changes the class attributes directly
    def changeName(cls, name): #cls is referring to the class
        cls.name=name #modifies the class attribute directly

p1=Person()
p1.changeName("himal")
print(p1.name)
print(Person.name)
