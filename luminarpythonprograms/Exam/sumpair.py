lst=[1,2,3,4]

element=int(input("enter the sum:"))
lst.sort()

low=0
upp=len(lst)-1

while(low<=upp):
    data=lst[low]+lst[upp]

    if(data==element):
        print("pairs are:",lst[low],lst[upp])
        break
    elif(data>element):
        upp=upp-1
    else:
        low=low+1