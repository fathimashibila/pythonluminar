num1=int(input("enter the value for num 1="))#10
num2=int(input("enter the value for num 2="))#20
num3=int(input("enter the value for num 3="))#15
if((num1>num2)|(num1<num3)):
    if(num2>num3):
        print("secondmax",num2)
    else:
        print("secondmax",num3)
elif ((num2 > num1) | (num2 < num3)):
    if (num1 > num3):
        print("secondmax", num1)
    else:
        print("secondmax", num3)

elif ((num3 > num1) | (num3 < num2)):
    if (num2 > num1):
        print("secondmax", num2)
    else:
        print("secondmax", num1)


else:
    print("numbers are equal")