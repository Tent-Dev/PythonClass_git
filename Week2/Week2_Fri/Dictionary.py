if __name__ == '__main__':
    student = {"id":"185214-5","name":"Adisak","Age":35}

print(type(student))
print(student)
print(student["id"])

student["weight"] = 30
student["id"] = "59122030-6"

print(student)

del student["id"]

print(student)
print("-"*100)
print(student.keys())
print("-"*100)
print(student.values())
print("-"*100)
print(student.items())

for i in student:
    print(i)

print("-"*100)

for key,val in student.items():
    print(key," : ",val)
