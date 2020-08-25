f=open("covid19","r")
dict={}
dict1={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    conf=data[8]
    death=data[7]

    if(state not in dict):
        dict[state]=conf
        dict1[state]=death
    else:
        dict[state]=conf
        dict1[state] = death
clist=[]
dlist=[]
deathsum=0
confsum=0
for k,v in dict.items():
    clist.append(int(v))
    #print(k,",","confirmed:",v)
    confsum+=int(v)
for k,v in dict1.items():
    dlist.append(int(v))
    #print(k,",","death",v)
    deathsum+=int(v)
for k,v in dict.items():
    if(max(clist)==int(v)):
        cstate,chighest=k,v
for k,v in dict1.items():
    if(max(dlist)==int(v)):
        dstate,dhighest=k,v


print("Total confirmed cases in India:",confsum)
print("Total death cases in India:",deathsum)
print("Highest confirmed case, state and count:",cstate,",",chighest)
print("Highest date case ,state and count:",dstate,",",dhighest)
