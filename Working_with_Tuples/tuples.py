# Tuples
# Tuples are not Mutable, they are immutable

# Concept of Mutable
list_1 = ['History' , 'Math' , 'Physics' , 'CompSci']
list_2 = list_1
list_1[0] = 'Art'
print(list_1)
print(list_2 , '\n') 


# Concept of Immutable
tuple_1 = ('History' , 'Math' , 'Physics' , 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

"""tuple_1[0] = 'Art'
print(tuple_1)
print(tuple_2)""" #TypeError: 'tuple' object does not support item assignment (means cannot be chnaged)

# Too add a value in list first we need to convert it into list and and revert it e.g:
temp = list(tuple_1)
temp.insert(0 , 'Arts')
tuple_1 = tuple(temp)
print(tuple_1)