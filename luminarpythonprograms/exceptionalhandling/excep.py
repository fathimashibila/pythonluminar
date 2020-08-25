# its an abnormal code or case
lst=[1,2,3,4]
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
try:# doubtfull code
    res=num1/num2
    print("result=",res)
    print("succesfully")
    position=int(input("enter the index:"))
    print(lst[position])

except Exception as e: #handling code
    print(e.args)
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))

finally:#clean up processing      mandotary
    print("we have data base transaction")
    print("file operation")