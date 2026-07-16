x="awesome"
def myvariable():
    print("python is " + x)
myvariable()

x="awesome"
def myvariable():
    x="fun"
    print("python is " +x)
myvariable()

def myvariable():
    global x
    x="awesome"
myvariable()
print("python is " +x)

x="awesome"
def myvariable():
    global x
    x="fun"
    print("python is " +x)
myvariable()