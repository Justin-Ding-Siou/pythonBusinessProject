# Function range(min_value, max_value, step) generates a sequence with numbers 
# min_value, min_value + 1, ..., max_value - 1. The last number is not included.

for i in range(5, 8):
    print(i, i ** 2)
print('end of loop\n')

# Default min_value: 0, step =1
for i in range(3):
    print(i)
print('end of loop\n')
    
# negative step
for i in range(10, 0, -2):
    print(i)
print('end of loop\n')
    
# empty sequence?
for i in range(-5):
    print(i)
print('end of loop\n')

for i in range(7, 3):
    print(i)
print('end of loop\n')