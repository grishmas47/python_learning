#implicit overloading
print(1+2) #add
print("hello"+"world") #concatenate
print([1,2,3]+[4,5,6]) #merge

class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img
    
    def showNum(self):
        print(self.real, "i+", self.img, "j")

    # def add(self,c2):
    #     newReal=self.real+c2.real
    #     newImg=self.img+c2.img
    #     return Complex(newReal, newImg)
    
    def __add__(self,c2): #dunder function
        newReal=self.real+c2.real
        newImg=self.img+c2.img
        return Complex(newReal, newImg)
    
    def __sub__(self,c2): 
        newReal=self.real-c2.real
        newImg=self.img-c2.img
        return Complex(newReal, newImg)

c1=Complex(3,5)
c1.showNum()

c2=Complex(3,2)
c2.showNum()

# num3=c1.add(c2)
# num3.showNum()

num3=c1+c2 #by using dunder function
num3.showNum()

num3=c1-c2
num3.showNum()
