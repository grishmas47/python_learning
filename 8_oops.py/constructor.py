class Student():
    name="malik"
    def __init__(self): #self is reference to current instance of the class
        print("adding new student into the database")

s1=Student() #automatically calls the init constructor

class Student():
    def __init__(self, fullname): 
        self.name=fullname #name is new variable created inside the class
        print("adding new student into the database")

s1=Student("karan")
print(s1.name)

s2=Student("aakash")
print(s2.name)

class Student():
    #default constructor
    def __init__(self): #self bahek aru paramter hudeina
        pass

    #parameterized constructor
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        print("adding data into the database")

s1=Student("karan", 98)
print(s1.name, s1.marks)

s2=Student("aakash", 87)
print(s2.name, s2.marks)