class Student:
    college_name="Bhar College"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def hello(self): #method
        print("hello student,", self.name)

    def get_marks(self):
        return self.marks

s1=Student("karan", 98)
s1.hello() #calling the method
print(s1.get_marks())

# Create student class that takes name and marks of 3 subjects as arguments in a constructor. Then create a method to print the average.
class Student():
    def __init__(self, name, emarks, mmarks, smarks):
        self.name=name
        self.emarks=emarks
        self.mmarks=mmarks
        self.smarks=smarks

    def avg(self):
        self.calc=(self.emarks+self.mmarks+self.smarks)/3
        return self.calc

s1=Student("mina", 87, 88, 95)
print(s1.name, s1.emarks, s1.mmarks, s1.smarks)
print(s1.avg())

s2=Student("railey", 90, 94, 89)
print(s2.name, s2.emarks, s2.mmarks, s2.smarks)
print(s2.avg())

s3=Student("steven", 95, 85,82)
print(s3.name, s3.emarks, s3.mmarks, s3.smarks)
print(s3.avg())

# OR
class Student:
    def __init__(self, name, marks): #marks as list
        self.name=name
        self.marks=marks

    def get_avg(self): #non-static methods
        sum=0
        for val in self.marks:
            sum=sum+val
        print("your name is", self.name, "you avg marks is", sum/3)

s1=Student("bishma", [98, 97, 94])
s1.get_avg()

s1.name="neema" #we can change attribute value directly as well
s1.get_avg()

#static methods: methods that dont use the self parameter
class Student:
    def __init__(self, name, marks): #marks as list
        self.name=name
        self.marks=marks

    @staticmethod #decorator: takes the hello function and changes its behaviour without modifying it
    def hello(): #static method; doesn't need object data
        print("hello")

    def get_avg(self): #non-static methods; needs object data self.marks
        sum=0
        for val in self.marks:
            sum=sum+val
        print("your name is", self.name, "you avg marks is", sum/3)

s1=Student("bishma", [98, 97, 94])
s1.get_avg()

s1.name="neema" #we can change attribute value directly as well
s1.get_avg()
s1.hello()
