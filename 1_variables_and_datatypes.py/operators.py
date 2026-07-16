#arithmetic operators
a=90
b=30
sum=a+b
print(sum)
print(a+b) #direct

diff=a-b
mul=a*b
div=a/b
print(diff)
print(mul)
print(div) #output in float

print(a % b) #remainder

a=2
b=2
print(a ** b) #a^b

#relational operators
a=30
b=20

print(a == b) #False
print(a != b) #True
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#assignment operators
num=10
num **=10
print("num:", num)

#logical operators
print(not True)
print(not False)

a=20
b=10
print(not a>b)

val1=True
val2=False
print("and operator:", val1 and val2) #True onlyif both variables are true

print("or operator:", val1 or val2) #False if both variables are false
print("or operator:", (a==b) or (a>b))