# print exercise
# https://realpython.com/python-formatted-output/

a = 123
b = 'abc'
c = 2/3

print(a, b, c)

# %-format
print("a=%4d, b=%s, c=%.3f" % (a, b, c))

# str-format: {i:4d} 第i個變數 4 digits
print("a={0:4d}, c={2:.3f}, b={1:2s}".format(a, b, c))

# f-format
print(f"a={a:>4d}, b={b:4s}, c={c:7.4f}")