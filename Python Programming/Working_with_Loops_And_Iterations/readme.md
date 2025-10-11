# 🔁 Python Loops and Control Flow — Complete Guide

This program demonstrates how **loops** work in Python, including concepts like:
- The `for` loop  
- The `while` loop  
- Using `enumerate()`  
- The `break` and `continue` statements  
- Nested loops (loops inside loops)  
- Infinite loops and how to control them  

These are fundamental tools in programming that allow you to repeat actions efficiently and control how your code runs under specific conditions.

---

## 📘 The `for` Loop in Python

The `for` loop is used to iterate (go through) sequences like lists, tuples, strings, or ranges.

Example:
```python
nums = [1, 2, 3, 4, 5]

for index, num in enumerate(nums, start=1):
    print(index, num)

Explanation:
	•	enumerate() returns both the index and value of each item in the list.
	•	By using start=1, the index begins from 1 instead of the default 0.

Output:

1 1
2 2
3 3
4 4
5 5

This is especially useful when you want both the position and the value while looping.

⸻

🧩 Important Keywords in Loops

Python provides two special keywords to control the flow of loops:
	1.	break
	2.	continue

⸻

🚫 The break Statement

The break statement immediately stops the loop once a specific condition is met.

Example:

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 4:
        print('Loop Terminated at reaching 4')
        break
    else:
        print(num)

Explanation:
	•	The loop goes through each number.
	•	When it reaches 4, the condition if num == 4 becomes True.
	•	The loop stops immediately, skipping any remaining numbers.

Output:

1
2
3
Loop Terminated at reaching 4


⸻

⏭️ The continue Statement

The continue statement skips the current iteration and moves to the next one.

Example:

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 4:
        print('Skipped the number', num, 'from the loop')
        continue
    else:
        print(num)

Explanation:
	•	When the loop encounters 4, the continue statement tells Python to skip the rest of the code in that iteration.
	•	The loop then continues with the next number (5).

Output:

1
2
3
Skipped the number 4 from the loop
5


⸻

🔁 Nested Loops (Loop within a Loop)

You can place one loop inside another to create combinations or repeat tasks multiple times.

Example:

nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)

Explanation:
	•	The outer loop iterates through the list of numbers.
	•	The inner loop iterates through each letter of 'abc'.
	•	For each number, the inner loop prints all letters.

Output:

1 a
1 b
1 c
2 a
2 b
2 c
...
5 a
5 b
5 c

This technique is often used in problems involving combinations or working with multiple lists.

⸻

🔢 Using range() in Loops

The range() function generates a sequence of numbers.
It’s commonly used with loops to repeat actions a certain number of times.

Example 1:

for i in range(10):
    print(i)

Output:
Prints numbers from 0 to 9.

Example 2:

for i in range(1, 11):
    print(i)

Output:
Prints numbers from 1 to 10.

⸻

🔄 While Loops

A while loop runs as long as a condition is True.
It stops only when the condition becomes False or when you use a break.

Example:

x = 0
while x < 10:
    print(x)
    x = x + 1  # or x += 1

Explanation:
	•	Starts with x = 0
	•	Keeps printing and incrementing x
	•	Stops automatically when x reaches 10 (condition x < 10 becomes False)

Output:

0
1
2
3
4
5
6
7
8
9


⸻

🧠 Using break in a While Loop

You can also manually stop a while loop using break.

Example:

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

Output:

0
1
2
3
4

Here, the loop stops when x becomes 5 — even though the condition (x < 10) is still True.

⸻

♾️ Infinite Loops

An infinite loop runs forever unless you stop it manually.
This happens when the condition always stays True, or when no break is used.

Example:

x = 0
while True:
    print(x)
    x += 1

Explanation:
	•	The condition True never becomes False.
	•	The loop will keep printing numbers endlessly.
	•	You must use a break statement or manually stop the program (e.g., press Ctrl + C in the terminal).

If we modify it like this:

x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1

The loop stops safely when x becomes 5.

⸻

🧩 Summary
	•	for loops are used to iterate through sequences (like lists or ranges).
	•	enumerate() helps get both index and value during looping.
	•	break stops the loop immediately.
	•	continue skips the current iteration and moves to the next.
	•	Nested loops help perform actions within actions.
	•	While loops run until a condition becomes False.
	•	Infinite loops must have a break condition to avoid running forever.

⸻

💡 Why Loops Are Important

Loops are essential in programming for:
	•	Automating repetitive tasks
	•	Processing large data sets
	•	Searching and filtering values
	•	Creating patterns and sequences
	•	Handling user input repeatedly

They are the backbone of automation and logic control in almost every Python program.

⸻

🏁 Conclusion

Understanding loops and flow control statements gives you the ability to make your programs dynamic and efficient.
By mastering for, while, break, and continue, you’ll have the foundational tools to handle logic-based problems, automate tasks, and build more powerful applications.
