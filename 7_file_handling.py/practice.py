# Create a new file and add the data.
f=open("practice.txt", "w")
f.write("Hi everyone")
f.write("\nwe are learning I/O")
f.write("\nusing Java.")
f.write("\nI like programming in Java")
f.close()

# # OR
# with open("practice.txt") as f:
#     f.write("Hi everyone")
#     f.write("\nwe are learning I/O")
#     f.write("\nusing Java.")
#     f.write("\nI like programming in Java")

# Replace all occurrences of Java with python in the file
with open("practice.txt", "r+") as f:
    data=f.read()
    print(data)

new_data=data.replace("Java", "python")
print(new_data) #ya samma practice.txt ma data write bhako chaina

with open("practice.txt", "w") as f:
    f.write(new_data)

# Search if the word "learning" exists in the file or not.
with open("practice.txt", "r") as f:
    data=f.read()
search=data.find("learning") #learning ka cha tesko index return garcha
print(search)

word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if data.find(word) != -1:
        print("Found")
    else:
        print("Not found")
    
# using function
def check(word):
    with open("practice.txt","r") as f:
        data=f.read()
        if data.find(word) != -1:
            print("Found")
        else:
            print("Not found")

check("learning")

# WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found
def check(word):
    data=True
    line_no=1
    with open("practice.txt", "r")as f:
        while data: #run till data ko value True hunu jel, teti bela samma line read gardai jane
            data=f.readline()
            if (word in data):
                print(line_no)
                return
            line_no+=1
    return -1

check("learning")

#From a file containing numbers seperated by comma, print the count of even numbers
count=0
with open("practice.txt", "w+") as f:
    data=f.write("2,3,4,5,6") #this is a string not an integer, anything read from a file is string
    f.seek(0) #moves the cursor to beginning of the file
    data=f.read()
    print(data)

    nums=data.split(",") #sabai number nikaleko through split and stores the numbers in a list
    print(nums)
    for val in nums:
        if(int(val) % 2 == 0): #type cast converting to integer
            print("even")
        else:
            print("odd")

    for val in nums:
        if(int(val) % 2 == 0):
            count+=1
    print(count)