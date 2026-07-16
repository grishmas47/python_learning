f=open("sample.txt", "w")
f.write("I am trying to learn javascript as well.")
f.close()

f=open("sample.txt", "a")
f.write("Then i will learn NodeJS")
f.close()

f=open("sample.txt", "a")
f.write("\nAfter that i will move to ReactJS")
f.close()

f=open("new.txt", "w") #edi file exist gardeina bhane naya file create huncha ra tesbhitra write garna milcha
f.close()