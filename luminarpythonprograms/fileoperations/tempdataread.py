f=open("tempedata","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    dis=data[0]
    temp=data[1]
    print(dis)
    print(temp)

    if(dis not in dict):
        dict[dis]=temp
    else:
        old=dict[dis]
        if(temp>old):
            dict[dis]=temp
print(dict)
for k,v in dict.items():
    print(k,",",v)

