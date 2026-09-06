#Tuple operations
t=(10,20,30,40)
print("Tuple element:",t[1])

#Set operations
s={1,2,3,4}
s.add(5)
s.remove(2)
print("Set:",s)

#Dictionary operation
student={"name":"Amit","age":20,"marks":85}

#Accessing values
print("Name:",student["name"])

#Updateing valus
student["marks"]=90

#Adding new key
student["city"]="Nagpur"

#Deleting key
del student ["age"]

print ("Updated Dictionary:",student)

#Built-in Function
print("Dictionary keys:",student.keys())
print("Dictionary values:",student.values())
print("Dictionary items:",student.items())
