lst=[]
print("enter the 3 numbers:")
for i in range(0,3):
    num=int(input())
    lst.append(num)
print("input list:",lst)
out=[0,0,0]
out[2]=lst[2]
out[1]=(lst[2]-lst[1])+out[2]
out[0]=(lst[1]-lst[0])+out[1]
print("output list:",out)