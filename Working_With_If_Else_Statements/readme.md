# 🧠 Python Conditional Statements — Complete Guide

This program demonstrates how **conditional statements** (`if`, `elif`, `else`) and **boolean logic** (`and`, `or`, `not`) work in Python.  
It also covers **object identity**, **false values**, and the difference between `==` and `is`.

---

## 📘 What Are Conditional Statements?

Conditional statements are used to make **decisions** in your Python programs.  
They allow your code to run **different blocks** depending on whether a condition is **True** or **False**.

### Syntax:
```python
if condition:
    # code runs if condition is True
elif another_condition:
    # code runs if the first condition is False but this one is True
else:
    # code runs if all above conditions are False


⸻

🧩 Simple If–Else Example

language = 'Python'

if language == 'Python':
    print('Language is Python')
else:
    print('No match')

	•	If the language variable equals "Python", the first block executes.
	•	Otherwise, it prints "No match".

⸻

🧱 Using elif for Multiple Conditions

If you want to test several possibilities, use elif (short for “else if”):

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

This checks each condition in order.
Only the first True condition will execute — the rest are ignored.

⸻

⚙️ Comparison Operators

Python supports several comparison operators used in conditions:
	•	Equal to: ==
	•	Not equal to: !=
	•	Greater than: >
	•	Less than: <
	•	Greater or equal: >=
	•	Less or equal: <=
	•	Object identity: is (checks if two variables point to the same memory location)

Example:

x = 10
y = 20

if x < y:
    print('x is smaller')


⸻

🔐 Boolean Operations (and, or, not)

Boolean operators are used to combine or modify conditions.

1. and → Both conditions must be True

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad creds')

2. or → Only one condition needs to be True

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad creds')

3. not → Reverses the truth value

if not logged_in:
    print('Please log in')
else:
    print('Welcome')


⸻

🧠 Object Identity vs Equality (is vs ==)

Python’s is and == are not the same.
	•	== checks values
	•	is checks memory identity

Example:

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True (same contents)
print(a is b)   # False (different memory locations)

print(id(a))    # e.g., 140351257303872
print(id(b))    # e.g., 140351257304448

When both variables point to the same object, is returns True:

a = [1, 2, 3]
b = a

print(a is b)   # True
print(id(a) == id(b))  # True


⸻

🚫 False Values in Python

In Python, certain values are automatically treated as False in conditions.

The following are considered False:
	•	False
	•	None
	•	0 (zero of any numeric type)
	•	Empty sequences: '', (), []
	•	Empty mappings: {}

Example:

condition = []

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

Output:

Evaluated to False


⸻

✅ Examples of Truthy and Falsy Values

condition = False     # False
condition = None      # False
condition = 0         # False
condition = 10        # True
condition = []        # False
condition = ''        # False
condition = {}        # False
condition = 'True'    # True (non-empty string)

In Python:
	•	Empty values → False
	•	Non-empty values → True

⸻

💡 Summary
	•	if, elif, and else let your program make decisions.
	•	Comparison operators (==, !=, >, <, >=, <=) check relationships between values.
	•	and, or, not combine or reverse logical conditions.
	•	== checks for value equality, while is checks for object identity.
	•	Certain values (like 0, None, '', [], {}) are falsy.
	•	Everything else is truthy.

⸻

🧩 Why Conditional Statements Matter

Conditional logic is the foundation of decision-making in programming.
They are essential for:
	•	Validating input
	•	Controlling program flow
	•	Managing authentication (like login systems)
	•	Building loops and logic-based functions

⸻

🏁 Conclusion

Understanding Python’s conditional statements, comparison operators, and boolean logic is key to writing dynamic and intelligent programs.
Mastering these basics will help you move toward more advanced topics like loops, functions, and control structures.

