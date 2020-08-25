employee={"id":1002,"name":"kamal","des":"tester","salary":1500}
print(employee["name"])
print("company" in employee)
employee["company"]="luminar"
print(employee)
employee["salary"]+=5000
for key in employee:
    print(key,",",employee[key])