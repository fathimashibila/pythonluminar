def factors(num):
    print("Factors of a number are: ")
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
number=320
factors(number)
