# # PROGRAM 1

feeling = input('How are you?')
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
print("\n")

# PROGRAM 2

m = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
m.sort()
print(m)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)


# PROGRAM 3

from operator import *
a = 1
b = 5.0
print('a = {}'.format(a))
print('b = {}'.format(b))
for func in (lt, le, eq, ne, ge, gt):
    print ('{}(a, b): {}'.format(func.__name__, func(a, b)))


# PROGRAM 4

str = "Py'thon"
print(str)
str2 = 'Py"thon'
print(str2)
print("\"okay\" sampai ketemu lagi")

teks = "Python adalah bahasa pemrograman yang powerfull.\nTerbukti Python bisa dijalankan di segala platform OS.\nJadi, saatnya kita menggunakan Python sebagai bahasa permrograman \nsehari-hari. Salam Python Dahsyat!"
print(teks)

kata = """Python adalah bahasa pemrograman yang powerfull.
# ... Terbukti Python bisa dijalankan di segala platform OS.
# ... Jadi, saatnya kita menggunakan Python sebagai bahasa pemrograman
# ... sehari-hari. Salam Python Dahsyat!"""
print(kata)

# PROGRAM 5

blog = "klinik" + "python"
print (blog)
new_blog = blog*5
print(new_blog)
blog *= 4
print(blog)
string = 'Klinik' 'Python'
print(string)

buah = 'Nanas'
print(buah[0])
print(buah[0:2])
print(buah[0:4])
print(buah[0:5])

# PROGRAM 6

a = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
# Bob'''
a = a.split("\n")
print(a)

# PROGRAM 7

z = [1, 3, 2, 4, 'Alice', 'Bob']
z = z.sort()
print(z)

print("Hello there!\nHow are you?\nI\'m doing fine.") 

multi_line = """Hello there!
How are you?
I'm fine."""
print(multi_line)

spam = ' Hello World '
print(spam)
x = spam.strip()
print (x)
y = spam.lstrip()
print(y)
z = spam.rstrip()
print(z)

print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))

# PROGRAM 8 

print("Hello world!".startswith("Hello"))
print("Hello world!".endswith("world!"))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello world!'.startswith('Hello world!'))
print('Hello world!'.endswith('Hello world!'))
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '=')) 