# if else statements
# Switch Case statement : it's a way to check multiple values


# Comparisions:
# Equal:              ==
# Not Equal:          !=
# Greater Than:        >
# Less Than:           <
# Greater or Equal:   >=    
# Less or Equal:      <=
# Object Identify:    is (To check wheather the values have same ID or memory)

language = 'Python'
if language == 'Python':
    print('Language is Python \n')
else:
    print('No match \n')


language = 'Java'
if language == 'Python':
    print('Language is Python \n')
else:
    print('No match \n')

# Elif

language = 'Java'
if language == 'Python':
    print('Language is Python \n')
elif language == 'Java':
    print('Language is Java \n')
elif language == 'JavaScript':
    print('Language is JavaScript \n')    
else:
    print('No match \n')
    
# Boolean Operations
# and
# or 
# not  

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page \n')
else:
    print('Bad creds \n')
    
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in: # Both should be true
    print('Admin Page \n')
else:
    print('Bad creds \n')



user = 'Admin'
logged_in = True

if user == 'Admin' or logged_in: # Only one should need to be true
    print('Admin Page \n')
else:
    print('Bad creds \n')


user = 'Admin'
logged_in = True

if not logged_in:
    print('Please log in')
else:
    print('Welcome\n')


user = 'Admin'
logged_in = False

if not logged_in:
    print('Please log in\n')
else:
    print('Welcome\n')
    
    
a = [1,2,3]
b = [1,2,3]
print(a == b)   
print(a is b) # these two are different objects in memory there locations are different
print(id(a))
print(id(b),'\n')
    
a = [1,2,3]
b = a
print(a is b) # because now the ID of a and b are same so it will return true
print(a == b, '\n')
print(id(a) == id(b), '\n') 
print(id(a))   
print(id(b) , '\n')




# False Values:
#     False
#     None
#     Zero of any numeric type
#     Any empty sequence. For example, '' , () , []
#     Any empty mapping. For example, {}
    
condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False \n')
    
    
condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False \n')


condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False\n')
    
    
condition = 10
if condition:
    print('Evaluated to True\n')
else:
    print('Evaluated to False\n')
    
    
condition = []
if condition:
    print('Evaluated to True\n')
else:
    print('Evaluated to False\n')
    
    
condition = ''
if condition:
    print('Evaluated to True\n')
else:
    print('Evaluated to False\n')
    
    
condition = {} # empty Dictionaries
if condition:
    print('Evaluated to True\n')
else:
    print('Evaluated to False\n')
    

condition = 'True'
if condition:
    print('Evaluated to True\n')
else:
    print('Evaluated to False\n')