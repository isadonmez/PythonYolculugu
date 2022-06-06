name = 'İsa'
surname = 'Donmez'
age = 27 #'27'

# print('My name is {}'.format(name))

# print('My name is {} {}'.format(name, surname))

# print('My name is {0} {1}'.format(name, surname))

# print('My name is {1} {0}'.format(name, surname))

# print('My name is {s} {n}'.format(n = name, s = surname))

print(" My name is {s} {n} and I am {a}".format(n = name, s = surname, a= age))
"""
formatta age değeri olarak girdiğimiz number değeri int olmasına rağmen format sayesinde str olarak algılanmaktadır.
"""

# result = 200/700
# print('the result is {r:7.10}'.format(r=result))

# print('the result is {r:7.5}'.format(r=result))

print(f"My name is {name} {surname} and I am {age} years old.")