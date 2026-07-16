#print the elements of the following list using a loop:
num=[1,4,9,16,25,36,49,64,81,100]
for val in num:
    print(val)

#search for a number x in this tuple using loop #linear search 
nums=(1,4,9,16,25,36,49,64,81,100,49)
x=4
index=0
for val in nums:
    if(val==x):
        print("x found at", index)
        break
    index=index+1
else:
    print("x not found")

#using while
index=0
while index<=len(nums)-1:
    if(nums[index]==x):
        print("x found at", index)
        break
    else:
        print("not found")
    index+=1
