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

s = {1,2,3,4,5,6,7,8,9}
print(s)
s.add(10) # Adds An Element
print(s)
s.remove(1) # Removes An Elements
print(s)
s.clear() # Empty The Sets
print(s)
s.pop() # Removes A Random Value
print(s)












