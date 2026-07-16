if 5>2:
    print("five is greater than two")
    print("two is smaller than five") #block of code must be in the same indentation level

age = 21

if (age >= 18):
    print("eligible for license")
    print("eligible for voting")

light = None

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

num = 4
if(num >=2 ):
    print("greater than 2")
elif( num >= 5):
    print("greater than 5")

age = 21

if(age >= 18):
    print("can vote") #indentation
else:
    print("cannot vote")

#Grading statements
marks = int(input("Enter your marks:"))

if(marks >= 90):
    print("Your grade is A")
elif(90 > marks and marks >= 80):
    print("Your grade is B")
elif(80 > marks and marks >= 70):
    print("Your grade is C")
else:
    print("Your grade is D")

#nesting
age = 81

if(age >= 18):
    if(age >=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

