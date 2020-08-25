from re import*
f=open("mailfile","r")

lst=[]
for line in f:
    words=line.rstrip("\n")
    lst.append(words)

print(lst)
rule='\w*[@]gmail.com'
for i in lst:
    matcher=fullmatch(rule,i)
    if (matcher!=None):
        print(i)