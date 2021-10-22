# List Comprehension 
# [ 運算式 for 元素 in 可迭代物件 if 挑件判斷]
number_list = [x for x in range(10)]
print(number_list)
print()

# add a condition
number_list = [x for x in range(10) if x % 2 == 0]
print(number_list)
print()

# nested conditions
number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(number_list)
print()

# generator comprehension
triangles = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
print(triangles)
print()

colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print (coloured_things)
print()

x = (x**2 for x in range(20))
print(list(x))
print()


