collection = {1,2,3,4}
print(collection)
print(type(collection))

collection1 = {1,2,3, 2.4, "hello", "world"}
print(collection1)

collection2 = {1,2,2,2, "hello", "hello"} #ignores the repeated values #output is unordered, no order
print(collection2)
print(len(collection2))

collection3 = {} #empty dictionary
print(type(collection3))

collection4 = set() #empty set
print(collection4)
print(type(collection4))