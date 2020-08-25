def add(**args):
    print(args)
    sum=0
    for k,v in args.items():
        sum=sum+v
    print(sum)
        


add(n1=10,n2=20,n3=30,n4=40)