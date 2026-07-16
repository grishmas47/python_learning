#1
words = {
    "table": {
        "a piece of furniture",
        "list of facts and figures"
    },
    "cat" : "a small animal"
}
print(words)

#OR
words = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}
print(words)

#2 You are given a list of sub for students. how many classes are required by all students?
subjects = {"python", "java", "C++", "python","javascript", "java", "python", "java", "C++", "javascript"}
print(len(subjects))

#WAP to enter marks of 3 students from the user and store them in a dictionary. Start with an empty dict and add marks one by one. Use subject name as key and marks as value.
data = {}
std1 = int(input("Enter your marks:"))
data.update({"phy": std1})

std2 = int(input("Enter your marks:"))
data.update({"chem": std2})

std3 = int(input("Enter your marks:"))
data.update({"maths": std3})

print(data)

#4 Figure out a way to print 9 and 9.0 as different number.
values = {9, 9.0, 9.99, "9.0"}
print(values)

#OR
values = { #using set
    ("float", 9.0), #wrapping inside tuple 
    ("int", 9)
}
print(values)