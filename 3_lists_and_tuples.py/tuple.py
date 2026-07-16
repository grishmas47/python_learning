tup = (1,2,3,4)
print(type(tup))
print(tup[0])

#tup[5] = 15 #ERROR

tup = () #empty tuple
print(tup)
print(type(tup))

tup = (1,) #single element tuple
print(tup)

tup=(1)
print(tup)
print(type(tup)) #python takes this as integer without comma

tup=(1,2,3,4,) #comma after last element rakhda ni huncha narakhda pani huncha
print(tup)

tup = (1,2,3,4) #slicing
print(tup[1:3])