# -*- coding: utf-8 -*-

import math

PI = math.pi

# Convert input string to integer
r = eval(input("Enter radius: "))

pe = 2 * PI * r
area = PI * (pow(r, 2))  # PI * (r**2)

print("Radius =  ", r)

# Print using %
print("\nPrint using %")

print("%9s = %.2f" % ("Radius", r))

print("Perimeter = %.2f" % pe)

print("%9s = %.2f" % ("Area", area))

# print using format
print("\nPrint using format")

# {index:format}
print("{0:>9} = {1:.2f}".format("Radius", r))

print("{0} = {1:.2f}".format("Perimeter", pe))

print("{0:>9} = {1:.2f}".format("Area", area))

# print using f-string http://zetcode.com/python/fstring/
print("\nPrint using f-string")

re_s = "Radius"
pe_s = "Perimeter"
ae_s = "Area"

print(f'{re_s:>9} = {r}')

print(f'{pe_s:>9} = {pe:.2f}')

print(f"{ae_s:>9} = {area:.2f}")
