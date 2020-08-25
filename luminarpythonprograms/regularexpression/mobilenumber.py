from re import*
rule='[7-9]\d{9}'
#/d{10}
num=input("enter the number:")
matcher=fullmatch(rule,num)
if(matcher!=None):
    print("valid no")
else:
    print("invalid no")