# methods in python list==11
#____________________
# append,reverse,copy,count,insert,remove,sort,pop,extend,index,clear
lst = [1, 3, 4, 5, 2]
lst.append(4)
print(lst)

lst = [1, 3, 4, 5, 2]
lst.reverse()
print(lst)

lst = [1, 3, 4, 5, 2]
a=lst.copy()
print(a)

lst = [1, 1, 4, 5, 2]
b=lst.count(1)
print(b)

lst = [1, 3, 4, 5, 2]
lst.insert(1,'cow')
print(lst)

lst = [1, 3, 4, 5, 2]
lst.remove(3)
print(lst)

lst = [1, 3, 4, 5, 2]
lst.sort()
print(lst)

lst = [1, 3, 4, 5, 2]
print(lst.pop(1))
print(lst)

lst = [1, 3, 4, 5, 2]
lst2=['cow','car','goat']
lst.extend(lst2)
print(lst)

lst = [1, 3, 4, 5, 2]
b=lst.index(5)
print(b)

lst = [1, 3, 4, 5, 4]
lst.remove(4)
print(lst)

lst = [1, 3, 4, 5, 2]
lst.clear()
print(lst)
