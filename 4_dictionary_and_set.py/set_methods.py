collection = set()
collection.add(1) #adds an element to the set
collection.add(2)
collection.add(2)
collection.add("gris") #string
collection.add((5,6,7)) #tuple #hashable value=immutable value
# collection.add([3,4,5]) #list #unhasable value=mutable, fututre ma same hash value nahuna sakcha, changeable hune bhayo
print(collection)

collection.remove(2) #removes an element from the set
#collection.remove(7) #error
print(collection)

collection.clear() #empties the set
print(collection)
print(len(collection))

collection = {"gris", 1, 2, "hello"}
collection.pop() #randomly selects a value to remove
print(collection)

set1 = {1,2,3,4}
set2 = {4,5}
print(set1.union(set2)) #combines both set values and returns a new value
print(set1.intersection(set2)) #combines common values and returns new value
 