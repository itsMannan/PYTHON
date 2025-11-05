🗂️ Python File Renaming Automation Script (Using os Module)

📘 Overview

This Python script demonstrates how to automate the process of renaming files inside a folder using Python’s built-in os module.

It walks through each step — from navigating into a directory to listing files, splitting names and extensions, cleaning up spaces, numbering with zero-padding, and finally renaming the files neatly.

Such scripts are very useful for organizing videos, images, documents, or datasets that follow inconsistent naming patterns.

For example, if your folder contains files like:

Sun - 1.mp4
Moon - 2.mp4
Star - 3.mp4

The script will automatically rename them to:

01-Sun.mp4
02-Moon.mp4
03-Star.mp4


⸻

🧩 Complete Code

import os

# to change my directory which contains all my files
os.chdir('/Users/m1-pro/Downloads/Videos')

"""print(os.getcwd())"""  # to check if we are in the correct directory or not

# to list everything in directory
for f in os.listdir():
    print(f)
    
# to split off the extension from the file name
for F in os.listdir():
    print(os.path.splitext(F))  # it will give us a tuple in which first part is carrying the name like ('Sun') and second part is carrying the extension like ('.mp4')
    
for f in os.listdir():
    file_name, file_extension = os.path.splitext(f)
    print(file_name)
    """print(file_extension)"""
    
for f in os.listdir():
    file_name, file_extension = os.path.splitext(f)
    print(file_name.split("-"))  # it will give us a list by splitting with hyphens
    
for f in os.listdir():
    file_name, file_extension = os.path.splitext(f)
    f_title , f_num = file_name.split('-')
    print(f_num)
    
# to print a formatted string
for f in os.listdir():
    f_name , f_ext = os.path.splitext(f)
    f_title , f_num = f_name.split('-')
    f_title =  f_title.strip()  # Remove the white space on left and right
    f_num  = f_num.strip()  # Remove the white space on left and right
    print(f'{f_num}-{f_title}{f_ext}')
    
print('\n')
  
for f in os.listdir():
    f_name , f_ext = os.path.splitext(f)
    f_title , f_num = f_name.split('-')
    f_title =  f_title.strip()  # Remove the white space on left and right
    f_num  = f_num.strip()[1:]  # Remove the white space on left and right
    print(f'{f_num}-{f_title}{f_ext}')
    
# To do a zero padded string there's a method for it called zfill
for f in os.listdir():
    f_name , f_ext = os.path.splitext(f)
    f_title , f_num = f_name.split('-')
    f_title =  f_title.strip()  # Remove the white space on left and right
    f_num  = f_num.strip()[1:].zfill(2)  # Remove the white space on left and right / Zfill to covert 1 into 01 and two means if there comes 10 it won't change it but if it is 2 or 3 it will add zero before them
    print(f'{f_num}-{f_title}{f_ext}')
    
print('\n')

for f in os.listdir():
    f_name , f_ext = os.path.splitext(f)
    f_title , f_num = f_name.split('-')
    f_title =  f_title.strip()  # Remove the white space on left and right
    f_num  = f_num.strip()[1:].zfill(2)  # Remove the white space on left and right / Zfill to covert 1 into 01 and two means if there comes 10 it won't change it but if it is 2 or 3 it will add zero before them
    new_name = f'{f_num}-{f_title}{f_ext}'
    
    os.rename(f , new_name)


⸻

🧠 Step-by-Step Explanation

1. Importing the os Module

import os

	•	The os module allows Python to interact with the operating system.
	•	It helps perform actions like navigating folders, renaming files, deleting files, and more.

⸻

2. Changing the Working Directory

os.chdir('/Users/m1-pro/Downloads/Videos')

	•	os.chdir() means Change Directory.
	•	You’re telling Python to switch into the folder where your video files exist.
	•	After this line, every command will execute inside that folder.

To confirm the directory:

print(os.getcwd())

This prints your current working directory, ensuring you’re in the right place.

⸻

3. Listing Files in the Directory

for f in os.listdir():
    print(f)

	•	os.listdir() lists everything in the current directory (files and folders).
	•	The loop prints the name of each file one by one.

Example output:

Sun - 1.mp4
Moon - 2.mp4
Star - 3.mp4


⸻

4. Splitting File Name and Extension

for F in os.listdir():
    print(os.path.splitext(F))

	•	os.path.splitext() splits a filename into two parts:
	1.	File name (without extension)
	2.	Extension (e.g. .mp4)
	•	Returns a tuple:

('Sun - 1', '.mp4')
('Moon - 2', '.mp4')
('Star - 3', '.mp4')



⸻

5. Extracting Only File Name

file_name, file_extension = os.path.splitext(f)
print(file_name)

	•	Unpacks the tuple into two variables:
	•	file_name: the text before .mp4
	•	file_extension: .mp4
	•	Prints just the name part.

⸻

6. Splitting File Name by Hyphen

print(file_name.split("-"))

	•	Splits the filename into parts using - as a separator.
	•	Returns a list:

['Sun ', ' 1']


	•	Spaces remain for now — we’ll clean them up later.

⸻

7. Separating Title and Number

f_title , f_num = file_name.split('-')

	•	Splits the name into two pieces:
	•	f_title: e.g. 'Sun '
	•	f_num: e.g. ' 1'
	•	Now you can access the title and number individually.

⸻

8. Removing Extra Spaces Using strip()

f_title = f_title.strip()
f_num = f_num.strip()

	•	Removes unnecessary spaces from both ends of the string.
	•	'Sun ' becomes 'Sun'.
	•	' 1' becomes '1'.

⸻

9. Printing a Formatted String

print(f'{f_num}-{f_title}{f_ext}')

	•	Uses f-strings for cleaner formatting.
	•	Prints file names as:

1-Sun.mp4
2-Moon.mp4
3-Star.mp4



⸻

10. Removing Unwanted Characters

f_num = f_num.strip()[1:]

	•	[1:] slices the string, removing the first character (like a space or symbol).
	•	Useful when numbers have extra characters (e.g. #1 → 1).

⸻

11. Adding Zero Padding with zfill()

f_num = f_num.strip()[1:].zfill(2)

	•	zfill(2) makes sure all numbers have two digits:
	•	1 → 01
	•	9 → 09
	•	10 → stays 10
	•	This ensures alphabetical and numerical sorting in the right order.

⸻

12. Creating a New File Name

new_name = f'{f_num}-{f_title}{f_ext}'

	•	Combines the cleaned title, number, and extension into a new consistent format:

01-Sun.mp4
02-Moon.mp4
03-Star.mp4



⸻

13. Renaming the Files

os.rename(f , new_name)

	•	Actually renames each file in your directory.
	•	The first argument f is the old name, and new_name is the new name.

⸻

14. Final Result Example

If your folder originally contained:

Sun - 1.mp4
Moon - 2.mp4
Star - 3.mp4

After running the script, it will automatically rename them as:

01-Sun.mp4
02-Moon.mp4
03-Star.mp4


⸻

⚙️ Key Python Methods Used

1. os
	•	Python’s built-in module for interacting with your system (folders, files, etc.).

2. os.chdir(path)
	•	Changes the current working directory to the path you specify.

3. os.getcwd()
	•	Returns the path of your current working directory.

4. os.listdir()
	•	Lists all files and folders in the current directory.

5. os.path.splitext(file)
	•	Splits a file name into (name, extension).

6. os.rename(old, new)
	•	Renames a file from the old name to the new name.

7. split('-')
	•	Divides a string wherever a hyphen appears.

8. strip()
	•	Removes spaces or extra characters from both ends of a string.

9. zfill(2)
	•	Adds leading zeros to make numbers two digits long (e.g. 1 → 01).

10. f-strings
	•	Used to insert variables directly into strings for easy formatting.

⸻

💡 Key Takeaways
	1.	The os module is powerful for file system automation.
	2.	You can manipulate file names using string functions like split(), strip(), and zfill().
	3.	Always test your renaming logic using print() before running os.rename() to avoid accidental file name changes.
	4.	This same logic can be applied to any bulk renaming — images, documents, datasets, etc.

⸻

⚠️ Important Precautions
	•	Always double-check your working directory before renaming.
	•	Use print(new_name) first to preview changes before actually renaming files.
	•	Keep a backup of your files before running any mass renaming script.

⸻

🏁 Final Thoughts

This project is a great hands-on example of Python automation using the os module.
It teaches:
	•	Directory navigation
	•	File listing and parsing
	•	String manipulation
	•	Practical automation for real-world use

Once you’re comfortable with this, you can expand the script to:
	•	Automatically sort files into folders based on file type
	•	Add timestamps to file names
	•	Rename files in multiple directories recursively

Python makes repetitive file tasks like this fast, efficient, and error-free — something that would otherwise take hours manually.
