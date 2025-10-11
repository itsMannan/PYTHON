📚 Python Lists – README

This file contains beginner-friendly examples that explain how lists work in Python.
A list is a collection of multiple items (numbers, words, etc.) stored in a single variable.
Lists are mutable, meaning you can change, add, or remove items anytime.

⸻

🧩 What is a List?

A list is written inside square brackets [].

Example:

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

Output:

['History', 'Math', 'Physics', 'CompSci']

You can also check how many items are inside your list using len():

print(len(courses))  # Output: 4


⸻

🎯 Accessing List Elements

Each element has an index number starting from 0.

print(courses[0])   # First element -> History
print(courses[3])   # Fourth element -> CompSci
print(courses[-1])  # Last element -> CompSci

⚠️ If you try to access something outside the list (like courses[4]), you’ll get an IndexError.

⸻

✂️ List Slicing

You can extract part of a list using slicing syntax [start:end].

print(courses[0:2])  # ['History', 'Math']
print(courses[:3])   # ['History', 'Math', 'Physics']
print(courses[2:])   # ['Physics', 'CompSci']

✅ Remember: slicing excludes the last index.

⸻

🧰 List Methods (Adding and Inserting)

You can easily modify lists using different methods.

course = ['History', 'Math', 'Physics', 'CompSci']
course.append('Arts')       # Adds to the end
course.insert(0, 'Urdu')    # Adds at specific position
print(course)

Output:

['Urdu', 'History', 'Math', 'Physics', 'CompSci', 'Arts']


⸻

🧺 Combining Lists

If you have two lists, you can merge them.

course = ['History', 'Math', 'Physics']
course_2 = ['Geography', 'English']

course.extend(course_2)
print(course)

Output:

['History', 'Math', 'Physics', 'Geography', 'English']

If you use append(course_2) instead of extend, it will add the second list as a single element:

['History', 'Math', 'Physics', ['Geography', 'English']]


⸻

❌ Removing Items

You can remove specific elements using:

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses)

Or remove the last item using pop():

subject = courses.pop()
print(subject)   # Returns 'CompSci'
print(courses)   # ['History', 'Math', 'Physics']


⸻

🔄 Sorting and Reversing Lists

To reverse or sort items:

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)

courses.sort()
print(courses)   # Alphabetical order

For numbers:

num = [9, 8, 7, 3, 11, 13, 15, 5, 10]
num.sort()
print(num)

To sort in descending order:

courses.sort(reverse=True)
num.sort(reverse=True)

You can also use sorted() if you don’t want to modify the original list:

sorted_courses = sorted(courses)


⸻

🔢 Min, Max, and Sum

You can do simple math with numeric lists:

num = [1, 5, 2, 4, 3]
print(min(num))  # 1
print(max(num))  # 5
print(sum(num))  # 15


⸻

🔍 Searching in Lists

Check if an item exists:

courses = ['History', 'Math', 'Physics', 'CompSci']
print('Art' in courses)     # False
print('Math' in courses)    # True

Find an item’s position:

print(courses.index('CompSci'))  # 3


⸻

🔁 Looping Through Lists

You can loop through all items:

for course in courses:
    print(course)

Or get both index and value using enumerate():

for index, course in enumerate(courses, start=1):
    print(index, course)

Output:

1 History
2 Math
3 Physics
4 CompSci


⸻

🔄 Converting Between Lists and Strings

Convert list → string using .join():

courses = ['History', 'Math', 'Physics', 'CompSci']
course_str = ", ".join(courses)
print(course_str)

Output:

History, Math, Physics, CompSci

Convert back string → list using .split():

new_list = course_str.split(', ')
print(new_list)


⸻

🧠 Some More List Examples

Example 1: Numeric List

numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(20)
print(numbers)

Output:

[10, 30, 40, 50, 60]

Example 2: Mixed Data List

student = ['Abdul', 22, 'AI Student', 3.8]
print(student)

Output:

['Abdul', 22, 'AI Student', 3.8]

Example 3: Nested List

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Accesses row 2, column 3

Output:

6


⸻

🧾 Summary in Simple Words
	•	Lists store multiple values in a single variable.
	•	They can hold different data types — strings, numbers, or even other lists.
	•	Use append() or insert() to add items.
	•	Use remove() or pop() to delete items.
	•	Use sort() and reverse() to organize your list.
	•	Use min(), max(), and sum() for number lists.
	•	Use join() and split() to move between lists and strings.
	•	You can loop through lists and even track both index and value with enumerate().
