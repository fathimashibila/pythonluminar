class Employe:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def printValue(self):
        print(self.name)
        print(self.age)
        print(self.sal)
    def __str__(self):        #here method overriding is happend ,this Emploee class (__str__) over rided Object class
        return self.name      #and displays object name
obj1=Employe("Rahul",22,25000)
obj2=Employe("vijay",23,30000)
obj3=Employe("vinu",24,35000)


ls=[]
lss=[]
ls.append(obj1)
ls.append(obj2)
ls.append(obj3)
for emp in ls:
    lss.append(emp.sal)
print(max(lss),emp)
