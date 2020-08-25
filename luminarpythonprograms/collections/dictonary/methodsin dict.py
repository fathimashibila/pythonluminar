# clear(),copy,fromkeys,get,items(),keys,pop(),popitem(),setdefault(),update(),values()

car={"brand":"ford","model":"mustang","year":1964}
car.clear()
print(car)

car={"brand":"ford","model":"mustang","year":1964}
a=car.copy()
print(a)

car={"brand":"ford","model":"mustang","year":1964}
v=12
z=car.fromkeys(car,v)
print(z)

car={"brand":"ford","model":"mustang","year":1964}
b=car.get("model")
print(b)
print(car["model"])

car={"brand":"ford","model":"mustang","year":1964}
x=car.items()
print(x)

car={"brand":"ford","model":"mustang","year":1964}
x=car.keys()
print(x)

car={"brand":"ford","model":"mustang","year":1964}
y=car.values()
print(y)

car={"brand":"ford","model":"mustang","year":1964}
car.pop("brand")
print(car)

car={"brand":"ford","model":"mustang","year":1964}
car.popitem()
print(car)     #removes last key value pair

car1={"brand":"ford","model":"mustang","year":1964}
x=car1.setdefault("month","2")
print(x)
print(car1)

car1={"brand":"ford","model":"mustang","year":1964}
car2={"color":"red"}
car1.update(car2)
print(car1)


car1={"brand":"ford","model":"mustang","year":1964}
v=car1.values()
print(v)