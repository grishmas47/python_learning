open("demo.txt") #if not in same folder, sabai path lekhnu parcha file ko
f=open("demo.txt", "w")
f.write("Hello")
f.write("\nMy name is G")
f.close()

f =  open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()
# comment

f =  open("demo.txt", "r")
data = f.read(5) #reads character from 0 to 4
print(data)
f.close()
# comment

f =  open("demo.txt", "r")
line1 = f.readline() #line1 pachi space aaucha because line 1 pachi\n huncha
print(line1)

line2 = f.readline() 
print(line2)
f.close()
# comment

f =  open("demo.txt", "r")
line2 = f.readline() #readline() reads one line at a time(until \n included) and python sees the data in a file as a single long string
print(line2) #prints displays the line and adds its own \n at the end
f.close()
#comment

f =  open("demo.txt", "r")
data=f.read()
print(data)
#cursor is at the end of life
line1 = f.readline() #empty space print bhairacha, nothing to read
print(line1)

f.seek(0)
line2 = f.readline()
print(line2)
f.close()
