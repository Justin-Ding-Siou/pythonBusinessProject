# validating local phone number, one number at a time
import re

# all the following formats are valid
phones = [
'(02) 2345-8738',
'(03) 463-8800',
'(03) 463 8800',
'(03) 4638800',
'02-2456-1009',
'02-26272389',
'02 2290 0318',
'03 435-2077',
'05 534 2601',
'06-2757575',
'08-723-4406',
'(082) 313-304',
'089-318855'
]

# Simple regex
print("First Try:")

regex = r'^\(?\d{2,3}\)? ?\d{4} ?\d{3,4}$'

for phone in phones:
  match = re.search(regex, phone)
  if match:
    print(phone)
print()


# More elaborated regex
regex2 = r'^\(?\d{2,3}\)?[ -]?\d{3,4}[ -]?\d{3,4}$'

# print(s)
print("Second Try:")
for phone in phones:
  match = re.search(regex2, phone)
  if match:
    print(phone)

