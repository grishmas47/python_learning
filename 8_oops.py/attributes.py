class Student():
    college_name="ABC College" #class attribute #can be used by any object #stored only once in memory

    def __init__(self, name, marks):
        self.name=name #object attribute #different name for different student
        self.marks=marks
        print("adding data into the database")

s1=Student("karan", 98)
print(s1.name, s1.marks)

s2=Student("aakash", 87)
print(s2.name, s2.marks)
print(s2.college_name)
print(Student.college_name)

class Student():
    college_name="ABC College" 
    name="Anonymous" #class attribute

    def __init__(self, name, marks):
        self.name=name #object attribute > class attribute
        self.marks=marks
        print("adding data into the database")

s1=Student("karan", 98)
print(s1.name, s1.marks)

s2=Student("aakash", 87)
print(s2.name, s2.marks)
print(s2.college_name)