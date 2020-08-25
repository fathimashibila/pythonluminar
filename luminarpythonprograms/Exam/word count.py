str="hello hai hello hai"
word=str.split(" ")
dict={}
for w in word:
    if w not in dict:
        dict[w]=1
    else:
        dict[w]+=1

print(dict)