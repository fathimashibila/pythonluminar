lst=[]
n=int(input("enter the limit of list:"))

print("enter the list elements:",end=" ")
for i in range(0,n):
    lst.append(int(input()))
print("input list:",lst)

for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(lst[j]>lst[j+1]):
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print("sorted lisit:",lst)