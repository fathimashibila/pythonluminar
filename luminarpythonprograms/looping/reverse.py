number=int(input("enter the number="))

rev=0
while(number!=0):
    reminder=number%10
    rev=(rev*10)+reminder

    number=number//10
print(rev)