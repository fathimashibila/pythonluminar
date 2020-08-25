lst=[1,2,3,4]
count=len(lst)
sum=int(input("enter the sum:"))
for i in lst:
    for j in lst:
        sumnum=i+j
        if (sum==sumnum):
            print("the numbers are:",i,j)
        else:
            pass
if(sum>(lst[count-1]*2)):
    print("not found")


