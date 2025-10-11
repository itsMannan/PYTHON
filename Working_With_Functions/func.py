# Function
# Functions are basically some instructions packaged together that perform a specific task

# to create function we use "def" keyword means defination

# pass: when we don't need to do anything in function but for the later use then we can use this pass keyword it will simply ignore this function and we can easily use that function in future and also it won't throw any errors

def hello_func():
    pass

print(hello_func) # this print out that this is a function with it's location in memory
print(hello_func()) # thats how it returns a value within a fuction but in this code it will show none as we are not returning anything

print('\n')


def hello_func():
    print('Hello Function!')
    
hello_func()
hello_func()
hello_func()
hello_func()
# Function help us to not repeat the code again and again

print('\n')

def hello_func():
    print('Hello Function.')
    
hello_func()
hello_func()
hello_func()
hello_func()

print('\n')

def hello_func():
    return 'Hello Function.'

hello_func() # does not print anything
print(hello_func())

print(len(hello_func()))
print(type(hello_func()))
print(hello_func().upper())

# Passing arguments to functions

def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('Hi'))
    
    
def hello_func(greeting): # greeting is a required argument
    return f'{greeting} Function.'

print(hello_func('Hi'))

print('\n')

def hello_func(greeting , name='You'): # default argument name='You'
    return f'{greeting}, {name}'

print(hello_func('Hi'))

print('\n')

def hello_func(greeting , name='You'): # default argument name='You'
    return f'{greeting}, {name}'

print(hello_func('Hi' , 'Abdul Mannan'))


print('\n')

def student_info(*args , **kwargs): # Positional arguments and keyword arguments
    print(args)
    print(kwargs)
    
student_info('Math' , 'Art' , name = 'John' , age = 22)


print('\n')

def student_info(*args , **kwargs): # Positional arguments and keyword arguments
    print(args) # takes arguments in tuple
    print(kwargs) # takes arguments in Dictionary form
    
courses=['Math' , 'Art']
info = {'name' : 'John' , 'age' : 22}
student_info(courses , info)


print('\n')

def student_info(*args , **kwargs): # Positional arguments and keyword arguments
    print('Positional Arguments: ',args) # takes arguments in tuple
    print('Keyword Arguments:',kwargs) # takes arguments in Dictionary form
    
courses=['Math' , 'Art']
info = {'name' : 'John' , 'age' : 22}
student_info(*courses , **info)


print('\n')

# Number of days per month. First value '0' is placeholder for indexing purposes.
month_days = [0 , 31 , 28 , 31 , 30 , 31 ,30 , 31 , 31 , 30 , 31 , 30 , 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years.""" # Dock string tells what class or function is doing
    return year % 4 == 0 and (year % 100 != 0 or year % 400 ==0)

def days_in_month(year , month):
    """Return number of days in that month in that year."""
    
    # year 2017
    # month 2
    if not 1 <= month <=12: # checks if month is between 1 - 12 
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2017))
print(is_leap(2019))
print(is_leap(2020))
print(is_leap(2030))


print('\n')

print(days_in_month(2017 , 2))
