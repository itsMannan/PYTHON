📘 Understanding Tuples in Python

Tuples are one of the most important and simple data structures in Python.
They look like lists, but there’s one major difference: tuples cannot be changed once created (they are immutable).

⸻

🔹 What is a Tuple?

A tuple is an ordered collection of items, written inside parentheses () and separated by commas.

Example:

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')

Tuples can store:
	•	Strings
	•	Numbers
	•	Booleans
	•	Even other tuples or lists

⸻

🔹 Mutable vs Immutable (Core Difference)

1. Mutable Objects — Lists

A mutable object can be modified after creation.

Example:

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
list_1[0] = 'Art'

print(list_1)
print(list_2)

Output:

['Art', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']

✅ Both lists changed because lists are mutable, meaning both variables point to the same data in memory.

⸻

2. Immutable Objects — Tuples

An immutable object cannot be modified after creation.

Example:

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

Output:

('History', 'Math', 'Physics', 'CompSci')
('History', 'Math', 'Physics', 'CompSci')

Now, if we try to modify it:

tuple_1[0] = 'Art'

❌ You’ll get this error:

TypeError: 'tuple' object does not support item assignment

That’s Python telling you:

“Tuples are immutable — you can’t change their values.”

⸻

🔹 Tuple Methods in Python

Because tuples are immutable, they have very few built-in methods compared to lists.

Here are the only two tuple methods you can use:

⸻

1. tuple.count(value)

This method returns the number of times a value appears in the tuple.

Example:

numbers = (1, 2, 3, 2, 2, 4)
print(numbers.count(2))

Output:

3

✅ Explanation:
There are three 2s in the tuple, so .count(2) returns 3.

⸻

2. tuple.index(value)

This method returns the index (position) of the first occurrence of a value in the tuple.

Example:

subjects = ('Math', 'Physics', 'History', 'Physics')
print(subjects.index('Physics'))

Output:

1

✅ Explanation:
The first time 'Physics' appears is at index 1 (since indexing starts at zero).

⸻

🔹 What You Cannot Do with Tuples

Since tuples are immutable:
	•	You cannot add items (append(), extend(), insert() won’t work)
	•	You cannot remove items (remove(), pop(), clear() won’t work)
	•	You cannot sort or reverse them directly (sort(), reverse() won’t work)

If you need to modify data, you must first convert the tuple into a list:

Example:

tuple_1 = ('Math', 'Physics', 'Chemistry')
temp_list = list(tuple_1)
temp_list.append('Biology')
tuple_1 = tuple(temp_list)
print(tuple_1)

Output:

('Math', 'Physics', 'Chemistry', 'Biology')

✅ Explanation:
You can’t modify tuples directly, but you can temporarily convert them into a list, make your changes, and convert back to a tuple.

⸻

🔹 When to Use Tuples Instead of Lists

Use tuples when:
	•	You don’t want data to change (like constants).
	•	You want slightly better performance (tuples are faster than lists).
	•	You want to use the data as dictionary keys (lists cannot be used as keys, but tuples can).

Example (using tuple as dictionary key):

location = {}
coordinates = (31.582, 74.329)
location[coordinates] = "Lahore, Pakistan"
print(location)

Output:

{(31.582, 74.329): 'Lahore, Pakistan'}


⸻

🔹 Summary
	•	Tuples are immutable, meaning they can’t be changed after creation.
	•	Lists are mutable, meaning they can be changed anytime.
	•	Tuples use (), lists use [].
	•	Only two tuple methods exist:
	•	.count(value) → counts occurrences
	•	.index(value) → finds position of a value
	•	You can convert a tuple to a list to modify it if needed.

⸻

🧩 Quick Example Recap

tuple_1 = ('Math', 'Physics', 'Chemistry')

# Counting
print(tuple_1.count('Math'))  # Output: 1

# Finding Index
print(tuple_1.index('Physics'))  # Output: 1

# Converting Tuple to List
temp = list(tuple_1)
temp.append('Biology')
tuple_1 = tuple(temp)
print(tuple_1)

Output:

1
1
('Math', 'Physics', 'Chemistry', 'Biology')
