#break
i=1
while i<=100:
    print(i)
    if(i==4):
        break #terminate the loop when i is 4
    i+=1
print("end of loop")

nums=(1,4,9,16,25,36,49,64,81,100)
i=0
x=64
while i < len(nums):
    if(nums[i]==x):
        print("found at index", i)
        break
    else:
        print("finding..")
    i+=1
print("end of loop")

# continue
i=0
while i <= 10:
    if(i==4):
        i+=1
        continue #skips 4
    print(i)
    i+=1

i=0
while i <= 10:
    if(i%2!=0):
        i += 1
        continue
    print(i)
    i+=1

#pass
for i in range(5):
    pass #no work inside loop #used for future; will complete in future

if i>5:
    pass

print("some future work")
