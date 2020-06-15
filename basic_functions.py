
def hello_func():       # leaving it blank
    pass

def hello_func():
    print('Hello function!')

def hello_func(greeting):
    return '{} function.'.format(greeting)
print(hello_func('Hi'))

def hello(greeting, name = 'you'):
    return '{}, {}.'.format(greeting, name)
print(hello('Hi'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', age: 22}
student_info(*courses, **info)
