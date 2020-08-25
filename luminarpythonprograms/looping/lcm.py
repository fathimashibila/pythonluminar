def lcm(x,y):
    if(x>y):
        large=x
    else:
        large=y
    while(True):
        if((large%x==0)and(large%y==0)):
            lcm=large
            break
        large+=1
    return lcm #if there is return then we call funtion with print or if we dont have return function then only call no print
num1=int(input("enter the number="))
num2=int(input("enter the number="))
print("lcm=",lcm(num1,num2))