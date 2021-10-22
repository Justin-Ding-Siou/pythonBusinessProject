# Iterate through a list

lst = [10, 50, 75, 84, 32]
 
# Using a for Loop
for x in lst: 
    print(x)
print("End using a for loop\n")

# Iterating using while loop 
while x < len(lst): 
    print(lst[x]) 
    x = x+1
print("End using a while loop\n")

# Using range() method
for x in range(len(lst)): 
    print(lst[x])
print("End using range() method\n")

# Using list comprehension
[print(x) for x in lst]
print("End using list comprehension\n")

# Using enumerate() method 
for i, v in enumerate(lst): 
    print (i,": ", v)
print("End using enumerate() method\n")

for _, v in enumerate(lst): 
    print (v)
print("End using enumerate() method\n")