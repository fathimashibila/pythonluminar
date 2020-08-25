str="ABABBBBBABCZAAAZZZZZZZZZ"
dict={}
for c in str:
    if(c not in dict):
        dict[c]=1
    else:
        dict[c]+=1
v=list(dict.values())
k=list(dict.keys())
print(k[v.index(max(v))])