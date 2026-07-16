class Student:
    def __init__(self, phy, chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3) + " % "

stu1=Student(98,97,99)
print(stu1.percentage)

stu1.phy=95
print(stu1.phy)
print(stu1.percentage) #doesnot change the percentage, original value nei set bhairakcha

class Student:
    def __init__(self, phy, chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math

    # def calcPercentage(self): #we can make different function/method if the value of attribute are not fixed
    #     self.percentage=str((self.phy+self.chem+self.math)/3) + " % "
    #     print("your percentage is", self.percentage)

    @property #by using property decorator
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + " % "

stu1=Student(98,97,99)
print(stu1.percentage)

stu1.phy=95
print(stu1.percentage)
#property is mainly used for derived or calculated values
#and when validation/control is necessary