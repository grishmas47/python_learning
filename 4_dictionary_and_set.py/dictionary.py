info = {
    "key": "value",
    "name": "gris", #string
    "learning":["python", "django"], #list
    "topics":("dict", "set"), #tuple
    "age": 22, #int
    "female?": True, #boolean
    "marks": [92,93,94],
    12.99: 92 #int as key
}
print(info)
print(type(info)) #returns dict
print(info["name"]) #display key inside dictionary
print(info["topics"])
#print(info["gpa"]) #error as it doesnot exist inside dictionary

info["name"] = "kailash" #overwrite
info["gpa"] = 4.0 #adding information
print(info)

null_dict = {}
null_dict["name"] = "mei"
print(null_dict)

#nested dictionary
student = {
    "name": "kailash",
    "subjects":{
        "phy" : 92,
        "chem": 95,
        "math" : 95
    }
}
print(student["subjects"]["chem"])