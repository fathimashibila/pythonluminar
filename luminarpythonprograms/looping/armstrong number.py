number=int(input("enter the number="))

cubesum=0
while(number!=0):
    digit=number%10
    cubesum=cubesum+(digit**3)

    number=number//10
print("Armstrong number=",cubesum)