#dictionary
#collection  name define different type of data
#             define   different type of data     duplicatesallowed        mutable          insertionorder preserved
#list           []      yes                            yes                   yes                    yes
#tuple           ()      yes                            yes                  no                     yes
#set             {}       yes                            no                  yes                     no
#dict            {}          yes                   no for keys but vales can       yesfor value       yes

student={"roll":20,"name":"tinu","age":50}
print(student["name"])
print(student["age"])

student={"roll":20,"name":"tinu","age":50}
for key in student:
    print(key,":",student[key])

#update
student={"roll":20,"name":"tinu","age":20}
student["age"]=25
print(student)
#to check total
print("total" in student)
#inset key value pair
student["total"]=150
print(student)





