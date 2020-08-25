from functools import *
lst=[1,2,3,4,5]
f=reduce(lambda num1,num2:num1+num2,lst)
print(f)
maxvalue=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(maxvalue)