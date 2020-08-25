class employee:
    def setEmployee(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
    def printEmploye(self):
        print(self.eid)
        print(self.ename)
        print(self.desig)


obj1=employee()
obj1.setEmployee(101,"tinu","tester",1000)
print(obj1.ename)
obj1.printEmploye()

obj2=employee()
obj2.setEmployee(102,"rahul","painter",2000)
obj2.printEmploye()
#self=it is a keyword used to point current class instance variable