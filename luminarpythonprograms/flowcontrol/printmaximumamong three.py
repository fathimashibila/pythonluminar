num1=int(input("enter the value for num 1="))
num2=int(input("enter the value for num 2="))
num3=int(input("enter the value for num 3="))
if((num1>=num2)&(num1>=num3)):
    print("max=",num1)
elif ((num2 >= num1) & (num2 >= num3)):
        print("max=", num2)
else:
    print("max=",num3)