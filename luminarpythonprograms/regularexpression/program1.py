from re import *
rule='[a-k][369][a-zA-Z0-9]'

varname=input("enter the variable name:")
matcher=fullmatch(rule,varname)

if(matcher!=None):
    print("valid")
else:
    print("invalid")