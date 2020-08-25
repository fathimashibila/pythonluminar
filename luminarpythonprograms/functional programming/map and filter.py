#map
lst=[1,2,3,4]

def square(num):
    return num*num
sq=list(map(square,lst))   #map(function,iterbable)
print(sq)


def evens(num):
    return num%2==0
even=list(filter(evens,lst))
print(even)
