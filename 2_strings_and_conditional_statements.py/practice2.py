#WAP to input first name and find its length
str = input("Enter your first name:")
print("length of first name is:", len(str))

# #WAP to find occurence of $ in string
str = "I $am studying $python"
print(str.count("$"))

#WAP to print if the number entered by the user is even or odd
num = int(input("Enter number:"))

if(num % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")

#WAP to find the greatest of 3numbers given by the user
num1 = int(input("Enter num 1:"))
num2 = int(input("Enter num 2:"))
num3 = int(input("Enter num 3:"))

if(num1 > num2 and num1 > num3):
    print("Num1 is greatest")
elif(num2 > num1 and num2 > num3):
    print("num2 is greatest")
else:
    print("num3 is greatest")

#WAP to check if a number is multiple of 7 or not
num = int(input("Enter number:"))

if(num % 7 == 0):
    print("The number is multiple of 7")
else:
    print("The number is not a multiple of 7")
