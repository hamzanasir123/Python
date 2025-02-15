# # Loop Means Repeat

# # Loop Are Used To Repeat Instructions

# # While Loop

# count = 1

# while count <= 5 :
#     print("Hello World")
#     count += 1


# # Practice Questions

# # 1 : Print Numbers 1 To 100

# i = 1
# while i <= 100 :
#     print(i)
#     i += 1

# # 2 : Print Numbers 100 To 1

# i = 100
# while i <= 1 :
#     print(i)
#     i -= 1

# # 3 : Print The Multiplication Table Of A Number n

# n = 1

# while n <= 10 :
#     print("2 *", n , " = " , n*2)
#     n += 1

# # 4 : Print the elements of the following list using a loop

# l = [1,4,9,16,25,36,49,64,81,100]
# indx = 0
# while indx < len(l) :
#     print(l[indx])
#     indx += 1

t = (1,4,9,16,25,36,49,64,81,100)
x = 64
idx = 0
while idx < len(t) :
    if(t[idx] == x) :
        print("x found on index ", idx)
    idx += 1


# Break And Continue


# Break
a = 1
while a >= 5 :
    print(a) 
    if(a == 3) :
        break
    a += 1

print("Loop End")


# Continue

c = 1
while c <= 5 :
    if(c == 3) :
        c += 1
        continue
    print(c)
    c += 1


# For Loop

# For Loops Are Used For Sequential Traversal.

numbers = [1,2,3,4,5,6,7,8,9]

for num in numbers :
    print(num)

friuts = ["Apple","Banana","Cherry","PineApple"]

for f in friuts :
    print(f)

str = "Hamza Nasir"

for char in str :
    print(char)


# Loop With Totally Optional Else

numbers = [1,2,3,4,5,6,7,8,9]

for num in numbers :
    print(num)
else : 
    print("End")


# Practice Question

a = [1,4,9,16,25,36,49,64,81,100]

for e in a: 
    print(e)

t = (1,4,9,16,25,36,49,64,81,100,49)
x = 49
idx = 0
for el in t:
    if(el == x):
        print("Number Found At Index :" , idx)
    idx += 1


# Range() function 

for i in range(10): 
    print(i)


# Range(Start?, Stop , Step?)

for i in range(10): # range(stop) 
    print(i)

print("Loop End")

for i in range(3, 10): # range(start? , stop) 
    print(i)
    
print("Loop End")

for i in range(3 ,100 , 3): # range(start? , stop , step?)
    print(i)

print("Loop End")


# Practice Questions

# Print numbers from 1 to 100

for i in range(101) :
    print(i)


# Print numbers from 100 to 1

for i in range(100,0,-1) :
    print(i)


# Print the multiplication table of a number n

n = int(input("Enter Number : "))

for i in range(1,11):
    print(n * i)


# Pass Statement

# Pass is a null statement that does nothing, it is used as a placeholder for future code

for el in range(10) :
    pass


# Practice Question 

n = 5
sum = 0
for num in range(n+1): 
        sum += num

print("Total Sum =", sum)


 