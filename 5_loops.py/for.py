num = [1,3,4,5]
for val in num:
    print(val)

items=["apple", "orange", "litchi"]
for elements in items:
    print(elements)

tup=(1,2,2,3,4,5,1)
for val in tup:
    print(val)

name = "bishma"
for char in name:
    print(char)

name = "valleyview"
for char in name:
    if(char == "i"):
        print("i found")
        break
    print(char)
else: #else always prints regardless of the condition so break is used
    print("END")