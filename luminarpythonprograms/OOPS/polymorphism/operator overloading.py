class Book:
    def __init__(self,pages):
        self.pages=pages
    def __sub__(self, other):            #this method is to overide + in class
        return (self.pages-other.pages)
    def __add__(self, other):               #put book() in the return to get sum of 3 number
        return Book(self.pages+other.pages)
    def __str__(self):
        return str(self.pages)

ob1=Book(100)
print(type(ob1))                           #both are class type(ob1)=class book
ob2=Book(200)
print(ob1+ob2)
print(ob1-ob2)
ob3=Book(100)
print(ob1+ob2+ob3)

