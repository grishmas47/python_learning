#print numbers from 1 to 100
i=1
while i <= 100:
    print(i)
    i += 1

#print numbers from 100 to 1
i=100
while i>= 1:
    print(i)
    i-=1

#print the multiplication table of number n
i=1
while i <= 10:
    n=2*i
    print(n)
    i += 1 

i=1
n=int(input("enter any number"))
while i<=10:
    print(n*i)
    i += 1

#print the elements of the following list using loop
nums=[1,4,9,16,25,36,49,64,81,100]
n=1 #without considering list
i=3
while n <= 100:
    print(n)
    n=n+i
    i += 2

index = 0 #travesing inside list
while index <= len(nums)-1:
    print(nums[index])
    index=index+1

#search for a number x in this tuple using loop
nums=(1,4,9,16,25,36,49,64,81,100,49)
index=0
x=49
while index <len(nums):
    print(nums[index]==x)
    index+=1

index=0
x=49
while index <len(nums):
    if(nums[index]==x):
        print("found at index", index)
    else:
        print("finding.")
    index+=1






