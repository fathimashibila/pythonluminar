f=open("wordcount","r")
dict={}
for line in f:
    words=line.rstrip("\n").split(" ")
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
print(dict)


#for k,v in dict.items():
   # print(k,",",v)
for key in dict:
    print(key,"," ,dict[key])