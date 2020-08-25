low=int(input("enter the lower limit="))
upper=int(input("enter the upper limit"))
evensum=0
for i in range(low,upper+1):
    if(i%2==0):
        evensum=evensum+1
    else:
        oddsum = oddsum + 1
print("even numbers are:",evensum)
print("odd numbers are:",oddsum)

