#validate vehicle registration number

from re import *
rule='[K][L][0-9]{2}[a-z]{2}\d{4}'
reg=input("enter the reg number:")
matcher=fullmatch(rule,reg)
if(matcher!=None):
    print("valid reg no")
else:
    print("invalid re no")



