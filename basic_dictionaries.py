
student = {'name':'John', 'age':29, 'courses':['Math', 'CompSci']}

print(student['name'])          # will give the value of the key
print(student.get('name'))      # will give the value of the key

print(student.get('phone', 'Not Found'))    # non existent keys will return No Found

student['phone'] = '555-5555'   # updating values
student['name'] = 'jane'        # updating values

student.update({'name':'ani', 'age': 22})   # updating values
print(student)

# del student['age']              # delete age key
age = student.pop('age')          # deletes age and returns it
print(age)

print(student.keys())             # prints out all the keys
print(student.items())            # prints both values and keys

for key in student:               # loop through all the items
    print(key)

for key, value in student.item():
    print(key, value)
