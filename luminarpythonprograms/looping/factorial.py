number=int(input("enter the number="))
i=0
factorial=1
if number<0:
    print("doesnot exit")
elif(number==0):
    print("one")
else:
    while(i<number):
       factorial=factorial*i
       i=i+1
    print(factorial)