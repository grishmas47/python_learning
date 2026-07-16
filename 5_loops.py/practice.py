#WAP to find sum of first n natural numbers (using while)
i=1
n=5
sum=0
while (i<=n):
    sum=sum+i
    i+=1
print(sum)

#(using for)
n=7
sum=0
for i in range(1, n+1):
    sum=sum+i
print("total sum:", sum)

#WAP to find the factorial of first n natural numbers (using for)
n=5
mul=1
for i in range(1,n+1):
    mul=mul*i
print("factorial is:", mul)

#using while
n=7
mul=1
i=1
while i<=n:
    mul=mul*i
    i+=1
print("fact is:", mul)

