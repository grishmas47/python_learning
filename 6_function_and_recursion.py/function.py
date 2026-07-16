def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum #returns the output

calc_sum(5,3)
#some more code
calc_sum(89,20)
#some more code
calc_sum(11,22)

# function definition 
def calc_sum(a,b): #parameters
    print(a+b)

#function call
sum = calc_sum(3,2) #argumets
print(sum) #none print huncha bcoz no return val

def print_hello(): #no parameter, no return
    print("hello")

print_hello()
print_hello()
print_hello()

def print_hello(): 
    print("hello")

output = print_hello()
print(output) #none bcoz the function doesnot return a value

#average of 3 numbers
def avg_num(a,b,c): #user defined functions
    avg=(a+b+c)/3
    print(avg)
    return avg

avg_num(4,2,6)

#built in functions
print("apple", "orange") #seperator: None = " "
print("banana")
print("orange") #end: None = "\n"

print("banana", end = " ")
print("orange")

print("banana", end = "$")
print("orange")

# default parameter
def cal_sum(a=2, b=3): #default parameter 
    print(a+b)
    return a+b

cal_sum()

def cal_sum(a, b=2): #always non-default arg follows default arg
    print(a+b)
    return a+b

cal_sum(4)
