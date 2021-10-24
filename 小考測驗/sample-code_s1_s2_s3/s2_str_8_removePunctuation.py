import string

s = "string, With. Punctuation?"
table = str.maketrans({key: None for key in string.punctuation})
new_s = s.translate(table)

print(new_s)