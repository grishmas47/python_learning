student = {     #nested dict
    "name": "vishu",
    "subjects":{
        "phy":98,
        "chem":97,
    },
    12:98
}
print(student.keys()) #nested bhitra ko keys return hudaina only outer keys return huncha

print(list(student.keys())) #type casting gareko
# print(float(student.keys())) #ERROR, float() argument must be a string or a number, not 'dict_keys', so dict_keys ma float use garna milena
print(len(student))
print(len(list(student.keys())))

print(student.values())
print(list(student.values())) #we can store list inside dictionary and vice versa

print(student.items()) #returns the key value pairs
print(list(student.items()))

pairs=list(student.items()) #accessing the key value pairs individually
print(pairs[0])
print(pairs[1])

print(student["name"]) #return the value of the key
print(student.get("name"))

# print(student["age"]) #error
# print(student.get("age")) #returns NONE

student.update({"city":"ktm"})
print(student)

new_dict={"city":"ktm", "age":17}
(student.update(new_dict))
print(student)

student.update({"name":"krishna"})
print(student)