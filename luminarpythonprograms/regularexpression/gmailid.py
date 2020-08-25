from re import *
rule='\w*[@]gmail.com'
mail=input("enter the mail:")
matcher=fullmatch(rule,mail)
if(matcher!=None):
    print("valid mail")
else:
    print("invalid mail")