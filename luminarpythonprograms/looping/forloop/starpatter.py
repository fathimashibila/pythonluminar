n=int(input("Enter the no of rows:"))
space=n-1
k=1
for i in range(n):
    print(" "*space + "*"*(k))
                                        #2space 1space 0space      #for 3 row             #m=n-1-i  or k=2*i+1
    space=space-1
    k=k+2                               #3spce   2space 1space 0space #for 4rows