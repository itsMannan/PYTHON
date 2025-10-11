🐍 Python Functions – Complete Guide

📘 Overview

This Python script is a complete demonstration of functions — how to define, call, and use them effectively in different ways.
It covers the basics of function creation, the purpose of the def keyword, the use of arguments, returning values, default parameters, and advanced concepts like positional and keyword arguments (*args and **kwargs).

It also includes practical examples such as calculating leap years and the number of days in a month.

⸻

🔹 1. What Are Functions?

Functions in Python are blocks of reusable code that perform a specific task.
Instead of repeating code multiple times, you can define a function once and call it whenever needed.
Functions improve code organization, reusability, and readability.

You define a function using the def keyword, followed by the function name and parentheses ().

def hello_func():
    print("Hello Function!")


⸻

🔹 2. The pass Keyword

When you want to define a function but don’t want it to do anything yet, you can use the pass keyword.
It acts as a placeholder so that Python doesn’t throw an error.

Example:

def hello_func():
    pass

The code will run successfully, even though the function body is empty.

⸻

🔹 3. Function Calls and Return Values

When a function is called, Python executes the block of code inside it.

Example:

def hello_func():
    print("Hello Function!")

hello_func()

You can also make a function return a value using the return statement:

def hello_func():
    return "Hello Function."

When you use print(hello_func()), the returned string will be displayed.
If you don’t use return, Python automatically returns None.

⸻

🔹 4. Benefits of Functions

Functions help you:
	•	Avoid repeating the same code multiple times.
	•	Make the code easier to read and maintain.
	•	Separate different logic into modular parts.

You can call a function as many times as you want instead of rewriting the same print statements again and again.

⸻

🔹 5. Working with Returned Values

When a function returns data, you can use it in other operations. For example:

print(len(hello_func()))        # Returns the length of the returned string
print(type(hello_func()))       # Shows the data type of the returned value
print(hello_func().upper())     # Converts the string to uppercase


⸻

🔹 6. Passing Arguments to Functions

Functions can accept inputs called arguments.
These arguments allow you to customize how the function behaves.

Example:

def hello_func(greeting):
    return f"{greeting} Function."

Here, greeting is a required argument that must be provided when calling the function:

print(hello_func("Hi"))


⸻

🔹 7. Default Arguments

You can set default values for parameters, so if the user doesn’t pass a value, the default one is used.

Example:

def hello_func(greeting, name='You'):
    return f"{greeting}, {name}"

If you call:

print(hello_func('Hi'))

Output:
Hi, You

If you call:

print(hello_func('Hi', 'Abdul Mannan'))

Output:
Hi, Abdul Mannan

⸻

🔹 8. Using *args and **kwargs

Python provides two special ways to handle a variable number of arguments:
	•	*args → used to pass multiple positional arguments (stored as a tuple)
	•	**kwargs → used to pass multiple keyword arguments (stored as a dictionary)

Example:

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)

Output:

('Math', 'Art')
{'name': 'John', 'age': 22}

You can also unpack data using * and ** when passing lists or dictionaries to a function:

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(*courses, **info)

This makes the list elements and dictionary keys automatically passed as arguments.

⸻

🔹 9. Practical Example – Days in a Month and Leap Year Checker

The code includes two practical functions that combine logic and reusability.

⸻

🧮 a) is_leap(year)

Checks whether a given year is a leap year or not.
A leap year occurs every 4 years, except for years divisible by 100 unless they are also divisible by 400.

Logic:

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

Example outputs:

print(is_leap(2020))  # True
print(is_leap(2019))  # False

Explanation:
	•	2020 → Divisible by 4 → Leap Year ✅
	•	2019 → Not divisible by 4 → Not a Leap Year ❌

⸻

📅 b) days_in_month(year, month)

Returns the number of days in a given month of a specific year.

It uses a predefined list of month days:

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	•	The 0 at index 0 acts as a placeholder for convenience (so January = index 1).
	•	If the month is February (month == 2) and it’s a leap year, it returns 29 days.
	•	If the month is invalid (not between 1–12), it returns "Invalid Month".

Example:

print(days_in_month(2020, 2))  # 29 (leap year)
print(days_in_month(2019, 2))  # 28
print(days_in_month(2025, 15)) # Invalid Month


⸻

🔹 10. Docstrings

The code also demonstrates docstrings, which are short documentation strings written inside triple quotes under a function definition.
They explain what the function does and can be accessed using the help() function in Python.

Example:

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

This makes it easier for others to understand your code without reading through the entire logic.

⸻

🔹 11. Summary

This code demonstrates:
	•	Creating functions with the def keyword.
	•	Using pass as a placeholder.
	•	Returning values using return.
	•	Passing arguments and using default values.
	•	Handling variable-length arguments with *args and **kwargs.
	•	Creating practical utility functions for checking leap years and month days.
	•	Using docstrings for self-documentation.

In short, this program gives you a strong foundational understanding of Python functions — from basic concepts to advanced argument handling — through clear examples and practical applications.

