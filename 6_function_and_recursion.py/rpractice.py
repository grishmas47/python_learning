#WARF to calculate sum of  first n natural numbers
def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n

print(sum(5))

#WARF to print all elements in a list
num = [2,5,6,7,3]

def ele(lst, idx):
    if(idx==len(lst)):
        return
    print(lst[idx], end=" ")
    ele(lst, idx+1)

ele(num, 0)