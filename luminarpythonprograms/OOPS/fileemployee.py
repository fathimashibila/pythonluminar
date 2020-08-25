class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary

        print(self.eid)
        print(self.ename)
        print(self.desig)
        print(self.salary)

    def __str__(self):
        return self.ename



f=open("file","r")
emplst=[]
for data in f:
    value=data.rstrip("\n").split(",")

    id=value[0]
    ename=value[1]
    desig=value[2]
    salary=value[3]
    obj=Employee(id,ename,desig,salary)
    emplst.append(obj)

for emp in emplst:
    print(emp)

#print all in caps
#print all employe name above 25000
#prove 5000 incre for all employee
