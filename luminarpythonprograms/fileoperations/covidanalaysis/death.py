# deaths
f=open("covid19","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    cases=data[7]
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases

for k,v in dict.items():
    print("State:",k,",","deaths:",v)


#highest death rate
val=list(dict.values())
data=max(val)
print(data)
highest=max(dict,key=dict.get)
print(highest,dict[highest])
#highest confirmed cases

#calculate total number of confirmed cases in india
#calculate total number of death in india