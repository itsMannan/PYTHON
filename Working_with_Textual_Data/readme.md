🐍 Python String Practice – README

This file contains simple Python code examples that help beginners understand strings in Python.
Each example explains how to work with text, modify it, and use helpful string functions.

⸻

📘 What is a String?

A string in Python is just a piece of text inside quotes.
Example:

message = "Hello World"

You can use:
	•	Double quotes "Hello"
	•	Single quotes 'Hello'
	•	Triple quotes """Hello""" for multi-line text.

⸻

🧩 Code Explanations

1. Printing Strings

message = "Hello World"
print(message)

➡️ This prints the message on the screen.

⸻

2. Handling Apostrophes in Strings

message2 = "Bobby's World"
message3 = 'Bobby\'s World'

➡️ The backslash \ allows us to include ' inside single quotes.

⸻

3. Multi-line Strings

message4 = """I'm doing the practise
of python from "Corey Schafer" channel on 
youtube"""
print(message4)

➡️ Triple quotes let you write multi-line text.

⸻

4. Finding String Length

message5 = 'Hello World'
print(len(message5))

➡️ len() shows how many characters are in the string (including spaces).

⸻

5. Accessing Characters (Indexing)

message6 = "Hello World"
print(message6[0])   # First letter: H
print(message7[10])  # Last letter: d

➡️ Indexing starts from 0.

⸻

6. String Slicing

message8 = "Hello World"
print(message8[0:5])   # Hello
print(message9[:5])    # Hello (same as above)
print(message10[6:])   # World

➡️ [start:end] → start included, end excluded.

⸻

7. Changing Case

print(message11.lower())  # hello world
print(message12.upper())  # HELLO WORLD


⸻

8. Counting Substrings

print(message13.count('l'))      # Counts how many times 'l' appears
print(message14.count('Hello'))  # Counts word 'Hello'


⸻

9. Finding Words

print(message15.find('World'))     # Returns index 6
print(message16.find('universe'))  # Returns -1 (not found)


⸻

10. Replacing Words

print(message17.replace('World', 'Universe'))

➡️ Creates a new string with the replacement.

⸻

11. String Concatenation

greeting = "Hello"
name = "Abdul Mannan"
message19 = greeting + ', ' + name
print(message19)

➡️ Use + to join strings.

⸻

12. Adding Extra Text

message20 = greeting + ', ' + name + '. Welcome:'
print(message20)


⸻

13. Using format() Method

message21 = '{} , {}, Welcome!'.format(greeting, name)
print(message21)

➡️ The {} placeholders are replaced by variables.

⸻

14. Using f-Strings (Modern Way)

message22 = f'{greeting} , {name.upper()}, Welcome!'
print(message22)

➡️ f-Strings are the easiest and most readable way to combine text and variables.

⸻

15. Exploring String Functions

print(dir(name))

➡️ Shows all the available string methods (like .upper(), .lower(), .replace(), etc.)

⸻

16. Getting Help

print(help(str))
print(help(str.lower))

➡️ help() gives information about how functions work.

⸻

🧠 Summary

Concept	Function	Example
Length	len()	len("Hello")
Lowercase	.lower()	"HELLO".lower()
Uppercase	.upper()	"hello".upper()
Count	.count()	"Hello".count('l')
Find	.find()	"Hello".find('e')
Replace	.replace()	"Hello".replace('H','Y')
Format	.format() / f''	f"Hi {name}"
Slice	text[start:end]	"Hello"[0:4] → Hell


⸻

🎯 Purpose of This Code

This practice file helps beginners:
	•	Understand how strings work in Python
	•	Learn string functions
	•	Practice indexing, slicing, and formatting

⸻
