#WAP to ask the user to enter names of 3 different movies and store them in a list
mov1 = input("Enter your favourite movie1:")
mov2 = input("Enter your favourite movie2:")
mov3 = input("Enter your favourite movie3:")
movies = [mov1, mov2, mov3]
print(movies)

#OR
movies = [] #empty list
mov1 = input("Enter your favourite movie:")
mov2 = input("Enter your favourite movie:")
mov3 = input("Enter your favourite movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#WAP to check if a list contains a palindrome of elements
num= list(input("Enter numbers/elements:"))
print(type(num))

num1 = num.copy() #it requires list not int or string
num1.reverse()

if(num1 == num):
    print("the list contains palindrome")
else:
    print("the list doesnot contain palindrome")

#WAP to count the numbers of students with the "A" grade in the tuple
grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A"))

#Store the above values in a list and sort then from "A" to "D"
grades_list = []
grades_list.append("C")
grades_list.append("D")
grades_list.append("A")
grades_list.append("A")
grades_list.append("B")
grades_list.append("B")
grades_list.append("A")
print(grades_list)

grades_list.sort()
print(grades_list)