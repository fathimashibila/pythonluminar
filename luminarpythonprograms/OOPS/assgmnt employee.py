#print all in caps
#print all employe name above 25000
#prove 5000 incre for all employee
class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary

        print("id=",self.eid)
        print("name=",self.ename)
        print("designation=",self.desig)
        print("salary=",self.salary)
        print("****************************")

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



data1=list(map(lambda e:e.ename.upper(),emplst))
print(data1)
data2=list(filter(lambda e:int(e.salary)>4000,emplst))
for e in data2:
    print(e)
data3=list(map(lambda e:int(e.salary)+5000,emplst))
print(data3)
salaryy=list(map(lambda emp:emp.salary,emplst))
print(max(salaryy))
per=list(filter(lambda e:e.salary==max(salaryy),emplst))
for i in per:
    print(i)
