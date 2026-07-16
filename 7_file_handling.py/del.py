f=open("new.txt", "w")
f.write("abc")
f.close()

import os #pre installed module
os.remove("new.txt")