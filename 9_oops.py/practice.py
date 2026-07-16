# class Circle:
#     def __init__(self, radius):
#         self.radius=radius

#     def area(self):
#         area=3.141*self.radius**2
#         return area
    
#     def perimeter(self):
#         peri=2*3.141*self.radius
#         return peri

# c1=Circle(6)
# print(c1.area())
# print(c1.perimeter())

# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary

#     def showDetails(self):
#         print("The employee's role is", self.role)
#         print("The employee is in", self.department, "department")
#         print("The employee's salary is", self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("JuniorDev", "Developer", 30000)

# e1=Engineer("Jude", 24)
# e1.showDetails()

class Order():
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, o2):
        return self.price > o2.price
        
o1=Order("Bag", 12000)
o2=Order("Watch", 70000)

print(o1>o2)
