language = 'Python'

if language == 'Python':
    print('Language is python')
elif language == 'Java':
    print('Language is java')
else:
    print('no match')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad Credentials')

if not logged_in:
    print('Please log in')
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)   # false cuz two different objects in memory
print(a == b)   # true

# False values in Python
# None.
# False.
# zero of any numeric type, for example, 0 , 0L , 0.0 , 0j .
# any empty sequence, for example, '' , () , [] .
# any empty mapping, for example, {} .

