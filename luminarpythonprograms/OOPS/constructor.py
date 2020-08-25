class employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def printEmploye(self):
        print(self.eid)
        print(self.ename)
        print(self.desig)
        print(self.salary)


obj1=employee(101,"tinu","tester",1000)
obj1.printEmploye()
print(obj1.salary)

obj2=employee(102,"rahul","painter",2000)
obj2.printEmploye()