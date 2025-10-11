# Sets
# Sets are values that are unordered and have no Duplicates values
# Sets don't care about order
# Uses of Sets is:
"""
->To test whether a value is part of a Set
->And Also it is used to remove duplicate values
"""

cs_courses = {'History' , 'Math' , 'Physics' ,'CompSci'}
print(type(cs_courses))
print(cs_courses)
print(len(cs_courses) , '\n')

# No repeating of values
cs_courses = {'History' , 'Math' , 'Physics' ,'CompSci' , 'Math'}
print(type(cs_courses))
print(cs_courses)
print(len(cs_courses) , '\n')

# Memeber ship test means check wheather the value is part of set or not
cs_courses = {'History' , 'Math' , 'Physics' ,'CompSci'}
print('Math' in cs_courses , '\n') # We can do that too for lists and Tuples but Sets are optimized for this method to check wheather the value is part of a set or not

# Sets can determine what values to share and not share with other sets
cs_courses = {'History' , 'Math' , 'Physics' ,'CompSci'}
art_courses = {'History' , 'Math' , 'Arts' , 'Design'}

# To check what values these sets have in common we use {.intersaction(value)}
print(cs_courses.intersection(art_courses),'\n')
# To check which values are not common in both sets we use difference method
print(cs_courses.difference(art_courses),'\n')
print(art_courses.difference(cs_courses),'\n')
# To add all values without repreation we use union
print(cs_courses.union(art_courses),'\n')

# Empty list
empt_list = []
empt_list = list()
print(empt_list)

# Empty Tuple
empt_tuple = ()
empt_tuple = tuple()
print(empt_tuple)

# Empty Sets
empt_set = {} # This is not right! it's a dictionary
empt_set = set() # This is the proper way to create empty set
print(empt_set)

# add in sets
my_set = {'Math', 'Physics'}
print(my_set)

my_set.add('CompSci')   # Adding a new element
print(my_set)

my_set.remove('Math')   # Removing an element
print(my_set)