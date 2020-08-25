#confirmed cases
f=open("covid19","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    cases=data[8]
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases
lst=[]
for k,v in dict.items():
    lst.append(int(v))
    print("State:",k,",","confirmed:",v)

high=max(lst)
print("highest confirmed cases:",high)

