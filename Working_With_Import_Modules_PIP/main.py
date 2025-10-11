import sys
sys.path.append('/Users/m1-pro/Desktop/my_module')

import IMP
import IMP as mm
from IMP import find_index # to use function itself from different module, it will only give us the access to use the function of that module 
from IMP import find_index , test
from IMP import find_index as fi , test
from IMP import * # it is used to import everything from module but it harder to track down where that function came from and it is a problem
import sys


courses = ['Computer' , 'Math' , 'Physics' , 'Science']

index = IMP.find_index(courses , 'Science')
print(index)
print(IMP.test , '\n')


courses = ['Computer' , 'Math' , 'Physics' , 'Science']

index = mm.find_index(courses , 'Physics')
print(index)
print(mm.test , '\n')


index = find_index(courses , 'Math')
print(index)
print(test , '\n')


index = fi(courses , 'Computer')
print(index)
print(test , '\n')

print('\n')

print(sys.path)


print('\n')

import random

courses = ['History' , 'Math' , 'Physics' , 'ComSci']

random_course = random.choice(courses)
print(random_course)



print('\n')

import math

courses = ['History' , 'Math' , 'Physics' , 'ComSci']

rads = math.radians(90)
print(math.sin(rads))


print('\n')

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))
print(calendar.isleap(2020))

courses = ['History' , 'Math' , 'Physics' , 'ComSci']


import os # this give us access to underlying operating system

print(os.getcwd()) # show what currently directory we are in (prints the current working directory)

print(os.__file__) 

import antigravity