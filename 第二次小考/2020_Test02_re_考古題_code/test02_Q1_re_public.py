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
'00886 943 123-123',
'886 943 123123',
'886 978 978 00',
'02886 978 978 000',
'000886 978 978 000',
'887 943 123 123',
'886 843 123 123',
'886 943 123 444',
'+886 943 444 123',
'886 0933 123 123'
]


# More elaborated regex

regex = r'^([\+]{1}|[0]{2})?\d{3}[ -]?\d{3}[ -]?\d{3}[ -]?\d{3}$'
# print(s)
print("First Try:")
for phone in phones:
  match = re.search(regex, phone)
  if match:
    print(phone)
print()
