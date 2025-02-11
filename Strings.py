str1 = "This is a string.\t We are creating it in python."
str2 = 'This is string with single quote.\nWe are creating it in python.'
str3 = """This is string with tripple quote."""

print(str1)
print(str2)

# Basic Operation 

# Concatination

print(str1 + " " + str2)

# Lenght Of String

print(len(str1))


# Indexing

name = "Hamza Nasir"

ch =  name[1]

print(ch)

# Slicing

print(name[1 : 5])
print(name[ : 5]) # [0 : 5]
print(name[3 : ]) # [3 : len[name]]

# Negative Index

fruit = "Apple"
print(fruit[-3 : -1]) # pl

# Strings Functions

str = "my name is hamza"
print(str.endswith("za"))
print(str.capitalize())
print(str.replace("a", "u"))
print(str.replace("hamza", "Hamza Nasir"))
print(str.find("a"))
print(str.count("a"))
