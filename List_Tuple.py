# List 

language = ["html", "css" , "Typescript", "Python"]
print(language)
print(type(language))
print(language[0])
print(language[1])
print(language[2])
print(len(language))


# Strings Are Immutable in Python
# List Are Mutable In Python You Can Access Them And Also Change Them

student = ["Hamza Nasir", 245369 , True]
student[2] = False
print(student)

# List Slicing

list = [1,2,3,4,5,6,7]
print(list[2:5]) # Ending Index Is Not Included


# List Methods

lists = [1,3,2]
lists.append(4)
print(lists)
lists.sort()
print(lists)
lists.sort(reverse=True)
print(lists)
lists.reverse()
print(lists)
lists.insert( 0 ,"Hamza")
print(lists)
lists.remove(3)
print(lists)
lists.pop(2)
print(lists)

# Tuples  

tup = (12,23,34,45,56,67) # Its Immutable Just Like strings
print(tup)
print(type(tup))
print(tup[2])

tups = (1,)
print(tup)
print(type(tup))


# Slicing Same As List

# Methods

a = (1,2,1,3,4,1)
print(a.index(3))
print(a.count(1))



