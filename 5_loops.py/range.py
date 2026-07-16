print(range(5))

seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

for i in seq:
    print(i)

for i in range(5): #stop
    print(i)

for i in range(2,5): #start, stop
    print(i)

for i in range(2,10,3): #start, stop, step
    print(i)

for i in range(2, 101, 2): #even numbers
    print(i)

for i in range(1,100,2): #odd numbers
    print(i)

#print numbers from 1 to 100
for val in range(1, 101, 1):
    print(val)

#print numbers from 100 to 1
for val in range(100, 0, -1):
    print(val)

# print multiplication table of number n
n=int(input("enter the number"))

for i in range(1, 10):
    print(n*i)

