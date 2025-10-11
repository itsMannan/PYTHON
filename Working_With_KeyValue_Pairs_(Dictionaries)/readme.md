🧠 Python Dictionaries — Detailed Explanation

This program demonstrates how Dictionaries work in Python. Dictionaries allow us to store and manage data in key–value pairs — making them one of the most useful and flexible data structures in Python.

⸻

📘 What is a Dictionary?

A Dictionary in Python is used to store data values in key–value pairs.
Each key is unique, and it is used to access the corresponding value.

Example:

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

Here:
	•	'name', 'age', and 'courses' are keys
	•	'John', 25, and ['Math', 'CompSci'] are their values

You can think of it like a real dictionary — where you look up a word (key) to find its meaning (value).

⸻

🧩 Accessing Values

To get a value, you use its key name in square brackets:

print(student['name'])     # Output: John
print(student['courses'])  # Output: ['Math', 'CompSci']

You can also use numbers as keys:

student = {1: 'John', 'age': 25}
print(student[1])  # Output: John


⸻

⚠️ Handling Missing Keys

If you try to access a key that doesn’t exist, Python throws an error:

print(student['phone'])  # ❌ KeyError

To avoid this, use the .get() method:

print(student.get('phone'))            # Output: None
print(student.get('phone', 'Not Found'))  # Output: Not Found

.get() safely returns a value if it exists, or a default message if it doesn’t.

⸻

🏗️ Adding and Updating Values

You can easily add new entries or update existing ones.

Adding a new key:

student['phone'] = '555-5555'

Updating an existing key:

student['name'] = 'Jane'

After adding and updating:

print(student)
# Output: {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}


⸻

🔁 Using the update() Method

The .update() method lets you change multiple key–value pairs at once:

student.update({'name': 'Jane', 'age': 26, 'phone': '444-44444'})

This updates 'name', 'age', and adds 'phone' if it doesn’t exist.

⸻

🗑️ Deleting Items

You can remove items in two ways:

1. Using del:

del student['age']

This permanently removes 'age' from the dictionary.

2. Using pop():

age = student.pop('age')
print(age)  # Output: 25

pop() removes the key and also returns its value — useful if you need it later.

⸻

🔍 Dictionary Information and Looping

You can find out useful information about the dictionary.

Length of dictionary:

print(len(student))  # Number of key–value pairs

Get all keys:

print(student.keys())

Get all values:

print(student.values())

Get both keys and values:

print(student.items())


⸻

🔄 Looping Through Dictionary

You can loop through all keys or both keys and values.

Only keys:

for key in student:
    print(key)

Output:

name
age
courses

Both keys and values:

for key, value in student.items():
    print(key, ':-', value)

Output:

name :- John
age :- 25
courses :- ['Math', 'CompSci']


⸻

🧠 Summary
	•	Dictionary = Key–Value pairs
	•	Keys are unique, values can repeat
	•	Use [] to access values, and .get() to avoid errors
	•	Add or update items using assignment (=) or .update()
	•	Remove items with del or .pop()
	•	Use .keys(), .values(), .items() to inspect the dictionary
	•	Use loops to go through keys and values efficiently

⸻

💡 Why Use Dictionaries?

Dictionaries are ideal when:
	•	You need fast lookups (searching by key is quick)
	•	You want to store structured data
	•	You want meaningful labels (keys) instead of numeric indexes

Example use cases:
	•	Student records
	•	Contact books
	•	Configuration data
	•	JSON-like data structures in APIs