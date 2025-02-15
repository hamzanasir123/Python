# set
# Set Are Unordered List

collections = {
    1,2,3,4,5, "Six" , "Seven" , "Eight"
}
print(collections)
print(type(collections))
print(len(collections))

collections = {
    1,2,3,4,5,5,2,3, "Six" , "Seven" , "Eight", "Six"
}
print(collections) # Its Ignores Double Values
print(type(collections))
print(len(collections))

# Empty Set

empty = {} # Thats Not How To Create Empty set it it dict
print(type(empty))

empty = set() # That's The Way 
print(type(empty))

# Set is Mutable But Set Element Is Inmutable


# Set Methods

e = {1,2,"Hamza","Nasir",3,4,5}

s = {1,2,3,4,5,6,7,8,9}
print(s)
s.add(10) # Adds An Element
print(s)
s.remove(1) # Removes An Elements
print(s)
s.pop() # Removes A Random Value
print(s)
print(s.intersection(e)) # Combines Common Values & Returns New
print(s.union(e)) # Combines Both Sets Values  & Returns New But Don't Changed Them
s.clear() # Empty The Sets
print(s)



# We Can Add Mutable Values In Set But Can't Add Immutable Values

# Practice Question 1

meanings = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
print(meanings)

# Practice Question 2

subjcts = {"python" , "java" , "C++" , "python" , "Javascript" , "java" ,"python", "java" , "C++" , "C"}

print("No Of ClassRoom We Need Is : ", len(subjcts))

# Practice Question 3

user = {}

math = int(input("Enter Marks For Math :"))
english = int(input("Enter Marks For English :"))
science = int(input("Enter Marks For Science :"))

user.update({"Math" : math})
user.update({"English" : english})
user.update({"Science" : science})


print(user)






