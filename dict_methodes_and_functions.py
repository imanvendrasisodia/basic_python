#dictionary is a data type of python which store multiple values in key and value pair. it is mutable (changes possible in original dictionary) and unordered (no index)
                # dict has unique key: but values are duplicated 
student = {
    "name":"ansh",
    "age": 18,
    "marks": 97
}
print(student)
print(student["name"])

print(student.keys())  #only show keys

print(student.values()) #only show values

print(student.items()) #key value pair print

print(student.get("name")) #value access

student.update({"city": "mathura", "colleges": " AKTU"}) #add ya update value
student.update({"college": "GL Bajaj"})
print(student)


student.pop("college") #to remove key:value pair
print(student)

student.popitem() # to remove last key:value pair
print(student)

new_cpy = student.copy() #duplicate dictionary
print(new_cpy)

student.setdefault("course", "python")
print(student)

temp = {
    "a": "gamma",
    "b": "alfa"

}
temp.clear() # to create a empty dict
print(temp)

# imp dict functions
print(len(student))
print(type(student))

