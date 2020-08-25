lst=[1,2,3,1,5,8]
newlst=[]
for i in lst:
    if i not in newlst:
        newlst.append(i)

print(newlst)
lst=[1,2,3,1,5,8,8,8]
newlstt=list(set(lst))
print(newlstt)