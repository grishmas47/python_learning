#recursive function
def show(n):
    if(n==0): #base case, like stopping condition in loops, otherwise infinitely run garcha
        return #return value chaideina, stop matra garne so only return, no return 0 or 1
    print(n)
    show(n-1) #show function bhitra nei tei function call gariracha
    print("end") #1 pachi kei kaam baki cha ki nai check garcha ra stack bata end print gardcha, similary with 2 3...

show(5) #5,4,3,2,1 lai ekei choti call garne

# factorial using recursion
# n!=(n-1)!*n #recurrence relation
# fact(n)=fact(n-1)*n
# fact(n-1)=fact(n-2)*(n-1)

def fact(n):
    if(n==0) or (n==1): #base case
        return 1 #value return garne bhayera 0!=1 value return garne
    return fact(n-1)*n #final value

print(fact(7))
