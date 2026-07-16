f=open("sample.txt", "r+")
f.write("hello bob") #suru bata overwrite huncha ra hellobob aaucha
print(f.read()) #cursor bob pachi cha, tei bhayera tespachi ko text matra read garcha #empty
f.close()

f=open("sample.txt", "w+")
print(f.read()) #kei pani read hudeina since w+ ma file truncate bhaidincha
f.close()

f=open("sample.txt", "w+")
f.write("mello")
print(f.read()) #kei pani print hudeina kina bhane cursor is at the end mello write bhayepachi

f.seek(0) #cursor moves at the beginning
print(f.read())
f.close()

f=open("demo.txt", "a+")
f.write("abcd")
f.close()

with open("demo.txt", "r")as f:
    data=f.read()
    print(data)

with open("demo.txt", "w") as f:
    data=f.write("HELLOO")
    print(data) #close garnu pardeina file automatically close huncha