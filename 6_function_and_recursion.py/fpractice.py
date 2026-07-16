# WAF to print length of a list
num = [2,4,5,6]
prime = [2,3,5,7,9]

def num_length(lst):
    length = len(lst)
    print(length)

num_length(num)
num_length(prime)

# WAF to print elements of a list in a single line
cities=["ktm", "pkr", "chitwan"]
#print(len(cities))
heroes = ["thor", "ironman", "spiderman"]
#print(cities[0], cities[1], cities[2])

def num_length(lst):
    i=0
    while(i<len(lst)):
        print(lst[i], end=" ")
        i+=1
    
num_length(cities)
num_length(heroes)

def num_length(lst):
    for item in lst:
        print(item, end=" ")

num_length(cities)

# WAF to print factorial of number n
def fact(n):
    i=1
    fact=n
    while(i<n):
        fact = fact*i
        i=i+1
    print(fact)
    return fact
fact(7)

def fact(n):
    i=1
    fact=1
    for i in range(i, n+1):
        fact=fact*i
    print(fact)
    return(fact)

fact(5)

# WAF to convert usd to npr
def mon_conversion(a):
    npr=a*151
    print(a, "USD value=", npr, "NPR")
    return npr

mon_conversion(30)

#odd or even
def odd_even(a):
    if(a%2==0):
        print("number is even")
    else:
        print("number is odd")

odd_even(5)
