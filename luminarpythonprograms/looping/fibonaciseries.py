terms=int(input("enter the no of terms="))
i=0
n1=0
n2=1
while(i<terms):
    print(n1,end=",")

    n3=n1+n2
    n1=n2
    n2=n3
    i+=1