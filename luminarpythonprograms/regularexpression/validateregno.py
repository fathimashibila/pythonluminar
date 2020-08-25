from re import*
f=open("regno","r")

lst=[]
for line in f:
    words=line.rstrip("\n")
    lst.append(words)

print(lst)
rule='[k][l][0-9]{2}[a-z]{2}\d{4}'
for i in lst:
    matcher=fullmatch(rule,i)
    if (matcher!=None):
        print(i)