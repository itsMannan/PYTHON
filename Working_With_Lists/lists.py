# List
# List Are Mutable

courses=['History' , 'Math' , 'Physics' , 'CompSci']
print(courses)
print(len(courses))

# List Slicing
print(courses[0])
print(courses[3])
print(courses[-1])
# print(courses[4]) throws an error list outof range

print(courses[0 : 2])

print(courses[:3])

print(courses[2:4])
print(courses[2:], '\n')

# List Methods
course=['History' , 'Math' , 'Physics' , 'CompSci']
print(course)
course.append('Arts') # add value at the end of List
course.insert(0 ,'Urdu') # to insert value on speacific index in List
print(course , '\n')

course=['History' , 'Math' , 'Physics' , 'CompSci']
course_2=['Geography' , 'English'] 
course.insert(0 ,course_2) # to insert value on speacific index in List
# this way it add a list within the
print(course , '\n')


course=['History' , 'Math' , 'Physics' , 'CompSci']
course_2=['Geography' , 'English'] 
course.extend(course_2) # to combine 2 list into one
print(course , '\n')


course=['History' , 'Math' , 'Physics' , 'CompSci']
course_2=['Geography' , 'English'] 
course.append(course_2) # to add a list within a list in the end
print(course , '\n')


# Remove values from Lists
courses = ['History' , 'Math' , 'Physics' , 'CompSci']
courses.remove('Math')
print(courses , '\n')

courses = ['History' , 'Math' , 'Physics' , 'CompSci']
subject = courses.pop() # By default this will remove the Last value from the list and can return it to some variable (Used in Stack and Queue)
print(subject)
print(courses , '\n')

# Sort our List
courses = ['History' , 'Math' , 'Physics' , 'CompSci']
courses.reverse() # to reverse the list
print(courses , '\n')

courses = ['History' , 'Math' , 'Physics' , 'CompSci']
courses.sort() # sort according to Alphabets or numbers
print(courses , '\n')

num = [9,8,7,3,11,13,15,5,10,12,1,2,4,6,14]
num.sort() # Sorted in Ascending order
print(type(num))
print(num , '\n')

num = [9,8,7,3,11,13,15,5,10,12,1,2,4,6,14]
courses = ['History' , 'Math' , 'Physics' , 'CompSci']
courses.sort(reverse=True) # sort according to Alphabets or numbers in Decending order
num.sort(reverse=True) # Sorted in decending order
print(type(num))
print(courses)
print(num , '\n')

# Checking MIN , MAX , SUM
courses = ['History' , 'Math' , 'Physics' , 'CompSci']
sorted_courses=sorted(courses)
print(sorted_courses , '\n')

num=[1,5,2,4,3]
print(min(num))
print(max(num))
print(sum(num), '\n')


courses=['History' , 'Math' , 'Physics' , 'CompSci']
print(courses.index('CompSci') , '\n')

courses=['History' , 'Math' , 'Physics' , 'CompSci']
print('Art' in courses)

courses=['History' , 'Math' , 'Physics' , 'CompSci']
print('Math' in courses , '\n')

for course in courses:
    print(course)
    
for index, course in enumerate(courses , start=1): # To access the index we use enumerate through which we can know the value is placed on which index, by default it starts from zero but we can change it and start it from 1 by changing in enumerate function
    #Enumerate Returns 2 values (index and value{Course} )
    print(index , course)
print('\n')   

# To Convert List into Strings we used a string method Called {.join()}
courses=['History' , 'Math' , 'Physics' , 'CompSci']
course_str = ", ".join(courses)
print(course_str) # Now it becomes a string of comma seperated
print(type(course_str), '\n')  

# To return a string into List
courses=['History' , 'Math' , 'Physics' , 'CompSci']
course_str = ", ".join(courses)
new_List=course_str.split(', ')
print(course_str) 
print(new_List)
