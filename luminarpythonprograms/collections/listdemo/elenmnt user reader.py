lst=[1,2,3,4,5,6,7,8,9,10,11,12]
element=int(input("enter the element to search:"))

flag=0
for i in lst:
    if(i==element):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("found")
elif(flag==0):
    print("not found")