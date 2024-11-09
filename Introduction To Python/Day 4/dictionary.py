# name ={key:value, key:value, key:value}
student={"name":"Fahim Chowdhury","Id":127,"batch":51,"Phn_number":"01991027456"}
print(student)
print(student["name"])
print(student.keys())
print(student.values())
student["address"]="Rajbari" # add
student["Id"]="2215151127" #update
del student["batch"] #delete
print(student)
for key,value in student.items():
    print(key,":",value)
print(list(student))
print(list(student.values()))