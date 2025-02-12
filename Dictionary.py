# Dictionary 
# Its Mutable
dict = {
    "name" : "Hamza Nasir",
    "age" : 24,
    "Roll No" : 245369 ,
    "Language" : ["html" , "css" ,"Typescript" , "Python"] ,
    "is Senior" : True,
}
print(dict)
print(type(dict))

# They Are UnOrdered

# Dont Allow Duplicate Keys

print(dict["name"])
print(dict["age"])
print(dict["is Senior"])

dict["age"] = 25
print(dict)

dict["surName"] = "Khan" # We Can Add New Key:Value Pair
print(dict)

# Nested Dictionary

student = {
    "name" : "Hamza Nasir",
    "subjects" : {
        "English" : 90,
        "Math" : 80,
        "Science" : 98 
    }
}
print(student)
print(student["subjects"]["Math"])


# Dictionary Methods

print(student.keys()) # Got All Keys
print(student.values()) # Got All Values
print(student.items()) # Got Keys And Values In Tuple
print(student.get("name2")) # No Error > None
#print(student["name2"]) # Error

student.update({"city" : "Karachi"})
print(student)




