# validating international mobile phone number, one number at a time
import re

phones = [
'00886 932 324 009',
'+886 932 345 009',
'886 932 345 009',
'886 932456009',
'886 932-456-567',
'886-978-978-000',
'+886 978-978-000',
'886 978-978000',
'886 978-978 000',
'886978978000',
'886 978 978 00',
'02886 978 978 000',
'000886 978 978 000',
'00886 943 123-123',
'886 943 123123',
'887 943 123 123',
'886 843 123 123',
'886 943 123 444',
'+886 943 444 123'
]

# Simple regex
print("First Try:")
regex = r'\+?\d{3} ?\d{3} ?\d{3} ?\d{3}$'
for phone in phones:
  match = re.search(regex, phone)
  if match:
    print(phone)
print()


# More elaborated regex

regex2 = r'^([\+]{1}|[0]{2})?\d{3}[ -]?\d{3}[ -]?\d{3}[ -]?\d{3}$'
# print(s)
print("Second Try:")
for phone in phones:
  match = re.search(regex2, phone)
  if match:
    print(phone)
print()

regex3 = r'^([\+]{1}|[0]{2})?886[ -]?9\d{2}[ -]?(?!444)\d{3}[ -]?(?!444)\d{3}$'
print("Third Try:")
for phone in phones:
  match = re.search(regex3, phone)
  if match:
    print(phone)