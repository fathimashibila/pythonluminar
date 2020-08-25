divy=9
divi=3
for i in range(1,9):
    if (i*divi>divy):
        break
q=i-1
print("quotient:",q)
rem=divy-(q*divi)
print("reminder:",rem)