# Dictionaries allow us to work with key value Pairs

# These are two linked values where the key is unique identifier where we can find our data and the value is that data


# Represent a student using Dictionaries
student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
print(student)


# Getting the value from one key
student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
print(student['name'])
print(student['courses'])


student = {1 : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
print(student[1])


"""student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
print(student['phone']) """ # throws an error 

#.get method returns a value or returns None 
student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
print(student.get('phone')) # this will not throws an error but instead it will tell you that the value your searching is not in this 

# Where as if we use this method for the value which is in the dictionary it will show you the out of that key value like
student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
print(student.get('name')) 


student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
print(student.get('phone' , 'Not Found'))

# Add a new entry in dictionary

student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
student['phone'] = '555-5555'
student['name'] = 'Jane' # shows updated value
print(student, '\n')

# Update value method
student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
student.update({'name' : 'Jane' , 'age' : 26 , 'phone' : '444-44444'})
print(student, '\n')

# To delete a specific key and it's value
student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
del student['age']
print(student, '\n')


student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
age = student.pop('age')
print(student)
print(age, '\n')

# How to Loop through all the keys and values of our dictionaries
student = {'name' : 'John' , 
           'age' : 25 ,
           'courses' : ['Math' , 'CompSci']}
print(len(student))
print(student.keys()) # returns only key values
print(student.values()) # return the values of key
print(student.items() , '\n') # return both key and their values


for key in student:
    print(key) # shows only key names like (name age courses)

print('\n')

for key , value in student.items():
    print(key , ':-' , value) # this method is use to print both key and value in loop