📘 Reading and Writing to Files in Python

🧩 Overview

This Python program demonstrates how to work with files using Python’s built-in functions and context managers.
You’ll learn how to:
	•	Open files in different modes (read, write, append)
	•	Read files in multiple ways
	•	Write and copy files safely
	•	Use the context manager (with statement) to handle files efficiently

⸻

⚙️ 1. Understanding the open() Function

The open() function is used to access files in Python.
It has the following syntax:

f = open('filename', 'mode')

🗂️ File Modes

Mode	Description	Behavior
'r'	Read	Opens file for reading (default mode). Error if file doesn’t exist.
'w'	Write	Opens file for writing (creates new file or overwrites existing one).
'a'	Append	Opens file for writing but adds new content at the end.
'r+'	Read + Write	Opens file for both reading and writing.

Example:

f = open('test.txt', 'r')  # Open for reading

If your file is in the same directory, you can simply mention its name (test.txt).
Otherwise, you must provide the full path (e.g., /Users/yourname/Documents/test.txt).

⸻

📄 2. Checking File Attributes

Once the file is opened, you can check its basic properties:

print(f.name)  # Prints the name of the file
print(f.mode)  # Shows the mode (r, w, a, etc.)

Always remember to close the file after using it:

f.close()

This step frees up system resources and prevents accidental data corruption.

⸻

🧠 3. Using Context Managers (with Statement)

Instead of manually opening and closing files, Python provides a safer and cleaner way — the context manager.

with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

✅ Benefits:
	•	Automatically closes the file after use (even if an error occurs).
	•	Makes your code cleaner and easier to read.

⸻

📚 4. Reading Data from Files

There are several methods to read data from a file.

🔹 a) Reading Entire Content

with open('test.txt', 'r') as f:
    contents = f.read()
    print(contents)

This reads the entire file as one long string.

⸻

🔹 b) Reading Lines as a List

with open('test.txt', 'r') as f:
    file_content = f.readlines()
    print(file_content)

This returns a list of lines, where each line is a separate string in the list.

Example output:

['Line 1\n', 'Line 2\n', 'Line 3\n']


⸻

🔹 c) Reading Line by Line

with open('test.txt', 'r') as f:
    line = f.readline()
    print(line, end='')

    line = f.readline()
    print(line, end='')

This reads one line at a time — useful when dealing with large files.

⸻

🔹 d) Using a Loop to Read All Lines

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

This method automatically reads each line until the end of the file — very memory-efficient!

⸻

⚡ 5. Reading Partial Data (Chunks)

Sometimes, you might not want to load the entire file at once — especially when dealing with large files.
You can specify how many characters (or bytes) to read at a time.

with open('test.txt', 'r') as f:
    f_contents = f.read(100)  # Reads first 100 characters
    print(f_contents)

Each subsequent call to f.read(100) continues reading the next 100 characters.

⸻

🔁 Reading a Large File in Chunks (Loop Method)

with open('test.txt', 'r') as f:
    size_to_read = 100
    f_content = f.read(size_to_read)
    
    while len(f_content) > 0:
        print(f_content, end='')
        f_content = f.read(size_to_read)

This loop continues reading until the file is completely read.

You can also visualize the chunks using markers (like *) to see progress:

with open('test.txt', 'r') as f:
    size_to_read = 10
    f_content = f.read(size_to_read)
    
    while len(f_content) > 0:
        print(f_content, end='*')
        f_content = f.read(size_to_read)


⸻

🧭 6. Using File Cursor with seek() and tell()

When you read a file, Python keeps track of where you are inside it — this is known as the file pointer (cursor).

▶️ Moving the Cursor — seek(position)

Moves the cursor back to a specific byte position.

📍 Getting Cursor Position — tell()

Returns the current byte position of the file pointer.

Example:

with open('test.txt', 'r') as f:
    f_content = f.read(10)
    print(f_content, end='')

    f.seek(0)  # Move cursor back to start
    f_content = f.read(10)
    print(f_content, end='')

    print('\n')
    print(f.tell())  # Shows current cursor position


⸻

✍️ 7. Writing to Files

To write data into files, use 'w' (write mode).

with open('test2.txt', 'w') as f:
    f.write('Hello World')

⚠️ Important Note:
	•	If the file does not exist, it will be created automatically.
	•	If it already exists, the old content will be overwritten.
	•	To avoid overwriting, use 'a' (append mode) instead.

Example:

with open('test2.txt', 'a') as f:
    f.write('\nThis is a new line')


⸻

🧪 Writing and Replacing Characters

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

Here:
	•	'Test' is written first.
	•	The cursor moves to the beginning (f.seek(0)).
	•	'R' overwrites the first letter — result: “Rest”

⸻

📂 8. Copying File Contents

We can copy content from one file to another using nested context managers:

with open('test.txt', 'r') as rf:       # Reading from original file
    with open('test_copy.txt', 'w') as wf:  # Writing to new file
        for line in rf:
            wf.write(line)

✅ This method:
	•	Reads each line from test.txt
	•	Writes it to a new file test_copy.txt
	•	Works efficiently even for large files

⸻

🧾 Summary

Task	Method/Command
Open a file	open('filename', 'mode')
Close a file	f.close()
Use context manager	with open(...) as f:
Read whole file	f.read()
Read one line	f.readline()
Read all lines	f.readlines()
Write to file	f.write('data')
Append to file	Open file in 'a' mode
Move cursor	f.seek(position)
Get cursor position	f.tell()
Copy file	Use nested with open() blocks


⸻

💡 Key Takeaways
	•	Always use context managers when working with files.
	•	Use 'r', 'w', 'a', 'r+' appropriately depending on your needs.
	•	To prevent overwriting files, prefer append ('a') mode or check before writing.
	•	seek() and tell() give you control over file reading and writing positions.
	•	Reading large files in chunks is more memory-efficient.

⸻

🧠 Example Workflow Recap
	1.	Open test.txt using open() or with.
	2.	Read content using read(), readline(), or readlines().
	3.	Write or copy contents into new files using 'w' or 'a' mode.
	4.	Use context managers for safety and clean code.
	5.	Use seek() and tell() to control cursor movement in files.
