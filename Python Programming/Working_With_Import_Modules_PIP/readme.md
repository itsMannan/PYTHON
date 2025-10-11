🐍 Python Module Import and Standard Library Demonstration

📄 Project Overview

This repository contains a detailed Python demonstration of how modules, imports, and Python’s standard libraries work.
It has been designed for beginners and intermediate learners who want to understand how Python handles:
	•	Custom module imports
	•	System paths
	•	Built-in modules like random, math, datetime, calendar, os, and even the fun hidden antigravity module!

👨‍💻 Author: Abdul Mannan
📅 Date: October 2025
🏷️ Category: Python Fundamentals / Learning Project

⸻

📘 Overview

This program demonstrates how modules and imports work in Python.
It covers the following topics:
	1.	Importing custom and built-in modules
	2.	Using sys.path to include external module directories
	3.	Different ways to import specific functions or variables
	4.	Using standard library modules like:
	•	random
	•	math
	•	datetime
	•	calendar
	•	os
	•	and even the fun hidden module antigravity 😄

It is a practice and demonstration code to understand how imports, paths, and Python’s standard libraries operate.

⸻

🧩 Code Explanation

1. Importing and Modifying the System Path

import sys
sys.path.append('/Users/m1-pro/Desktop/my_module')

	•	sys is a built-in Python module that gives access to system-specific parameters and functions.
	•	sys.path is a list of directories where Python looks for modules when you try to import them.
	•	Using sys.path.append(), we are manually adding a directory (/Users/m1-pro/Desktop/my_module) so that Python can find and import our custom module located there.

✅ Why this is important:
If your module isn’t in the same folder as your main Python file, you must tell Python where to find it. That’s what sys.path.append() does.

⸻

2. Importing a Custom Module (IMP)

import IMP
import IMP as mm
from IMP import find_index
from IMP import find_index , test
from IMP import find_index as fi , test
from IMP import *

Let’s break this step by step 👇

a) import IMP
	•	Imports the whole module named IMP.
	•	Now, to use anything from this module, we prefix it with IMP. — like IMP.find_index().

b) import IMP as mm
	•	Imports the same module but gives it a shorter alias name (mm).
	•	Now, we can use mm.find_index() instead of writing IMP.find_index() every time.

c) from IMP import find_index
	•	Imports only the specific function find_index from the module IMP.
	•	After this line, we can use find_index() directly without writing IMP..

d) from IMP import find_index , test
	•	Imports both find_index (a function) and test (a variable or function) from the module.

e) from IMP import find_index as fi , test
	•	Renames find_index to fi locally, which is useful if you have multiple functions with the same name in different modules.

f) from IMP import *
	•	Imports everything (all functions, variables, classes) from the module.
⚠️ Warning: It’s usually not recommended because it becomes hard to track where a function or variable came from.

⸻

3. Using the Imported Functions and Variables

courses = ['Computer' , 'Math' , 'Physics' , 'Science']

index = IMP.find_index(courses , 'Science')
print(index)
print(IMP.test , '\n')

	•	courses is a list of course names.
	•	IMP.find_index() searches for 'Science' in the list and returns its index.
	•	IMP.test prints a variable named test from the IMP module (maybe a string or number defined there).

⸻

4. Accessing with the Alias mm

courses = ['Computer' , 'Math' , 'Physics' , 'Science']

index = mm.find_index(courses , 'Physics')
print(index)
print(mm.test , '\n')

	•	Same list, but now using the alias name mm instead of IMP.
	•	Performs the same operation as before.

⸻

5. Accessing the Function Directly (Without Module Prefix)

index = find_index(courses , 'Math')
print(index)
print(test , '\n')

	•	Because we imported these directly using from IMP import find_index, test,
we can now use them without the module name.

⸻

6. Using the Renamed Function (fi)

index = fi(courses , 'Computer')
print(index)
print(test , '\n')

	•	Same function, but through its alias name fi.
	•	Prints the index of 'Computer' and the test variable.

⸻

7. Viewing Python’s Search Path

print('\n')
print(sys.path)
print('\n')

	•	Prints all the directories where Python searches for modules.
	•	Useful for debugging when Python says “ModuleNotFoundError”.

⸻

8. Using the random Module

import random

courses = ['History' , 'Math' , 'Physics' , 'ComSci']

random_course = random.choice(courses)
print(random_course)

	•	random is a standard library for generating random numbers or picking random items.
	•	random.choice(courses) randomly selects one course from the list.

⸻

9. Using the math Module

import math

courses = ['History' , 'Math' , 'Physics' , 'ComSci']

rads = math.radians(90)
print(math.sin(rads))

	•	The math module provides mathematical functions.
	•	math.radians(90) converts 90 degrees into radians.
	•	math.sin(rads) calculates the sine of 90°, which is approximately 1.0.

⸻

10. Using datetime and calendar Modules

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))
print(calendar.isleap(2020))

	•	datetime.date.today() gives today’s date.
	•	calendar.isleap(year) checks if a given year is a leap year.
	•	2017 → False, 2020 → True

⸻

11. Using the os Module

import os

print(os.getcwd())
print(os.__file__)

	•	os gives access to Operating System functions.
	•	os.getcwd() → Prints the current working directory.
	•	os.__file__ → Shows the location of the os module on your computer.

⸻

12. The Fun Easter Egg: antigravity

import antigravity

	•	This is a hidden fun module in Python 🪄.
	•	When imported, it opens a web browser showing a famous XKCD comic about Python and flying.

⸻

⚙️ Summary of All Modules Used

Module	Type	Purpose
sys	Built-in	Manage Python runtime environment (e.g., module search paths)
IMP	Custom	Demonstration of user-defined module and function imports
random	Built-in	Generate random selections and numbers
math	Built-in	Perform mathematical calculations
datetime	Built-in	Work with dates and times
calendar	Built-in	Check leap years, generate calendars
os	Built-in	Interact with the operating system (paths, directories)
antigravity	Built-in	Opens a fun comic in your browser 😄


⸻

🧠 Key Takeaways
	•	sys.path.append() helps Python locate custom modules.
	•	You can import:
	•	Entire modules → import module
	•	With alias → import module as alias
	•	Specific functions → from module import function
	•	All items → from module import * (⚠️ not recommended)
	•	Python provides many powerful standard libraries ready to use.
	•	The antigravity module is a fun Easter egg in Python.

⸻

🧾 Example Output (may vary)

3
some test value

2
some test value

1
some test value

0
some test value

['/Users/m1-pro/Desktop/my_module', '/usr/local/lib/python3.11', ...]

Physics
1.0
2025-10-09
False
True
/Users/m1-pro/Desktop
/usr/lib/python3.11/os.py


⸻

💡 Conclusion

This code serves as a practical example of how Python handles imports, paths, and standard modules.
By understanding this, you’ll be able to:
	•	Organize your projects better
	•	Reuse code efficiently
	•	Explore Python’s rich standard library with confidence 💪
