number=int(input("enter the number="))
n=number
rev=0
while(number!=0):
    reminder=number%10
    rev=(rev*10)+reminder

    number=number//10
if(n==rev):
    print("palindrome")
else:
    print("not palindrome")