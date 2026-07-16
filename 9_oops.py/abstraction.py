#Abstraction: Hiding the implementation details of a class and only showing the needed/imp features to the user
class Car():
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start_car(self):
        self.acc=True
        self.clutch=True
        print("Car started....")

c1=Car()
c1.start_car() #only necessary detail i.e car started