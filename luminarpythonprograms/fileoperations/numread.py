f=open("numbers","r")
lst=[]
for num in f:
    lst.append(int(num.rstrip("\n")))  #rstrip for removimg terminal letter
print(lst) #lstrip
result=sum(lst)
print(result)