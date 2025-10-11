# OS module allows us to interact with the underlying operating system in several different ways like:
"""
1. navigate the file system
2. get file information
3. look up and change the environment variables
4. move files around
"""

import os # built-in module

print(dir(os) , '\n') # this will show us all the attributes or methods we can use from this imported module

# to print current working directory we write it as:
print(os.getcwd() , '\n') 

# To navigate to a new location on the filesystem
# navigate to desktop

os.chdir('/Users/m1-pro/Desktop/')
print(os.getcwd() , '\n') # changed our directory from Python programminf to desktop


# to see what file and folders are on the desktop we can use method
print(os.listdir(),'\n') 


# to create a new folder on desktop 'like os-demo-2'
"""os.mkdir('OS-demo-2/Sub-Dir-1')""" # if we just want to make folder 

# if we want to make folder within a folder
"""os.makedirs('OS-demo-2/Sub-Dir-1')""" #I have commented it because when i ran it again it throws an error of file existing 
print(os.listdir(),'\n')

# To Delete these folders
"""os.rmdir('OS-demo-2/Sub-Dir-1')""" # it will not remove intermediate directories
"""os.removedirs('OS-demo-2/Sub-Dir-1') {commenting this because it already deleted the file and if I don't comment it, it will throws an error}""" # it will remove your intermediate directories

print(os.listdir(),'\n')


# To rename a file or folder

'''os.rename('intro.py' , 'First_python_code.py')''' # to rename file it is compulsory to pass first the orginal file or folder name and then new name of file or folder
print(os.listdir(), '\n') 

# to look at some information about our files
print(os.stat('First_python_code.py'))
print(os.stat('First_python_code.py').st_size)
print(os.stat('First_python_code.py').st_mtime) # prints timestamp

# to get timestamp in human readable format we use this method to get the actual date and time
from datetime import datetime
mod_time = os.stat('First_python_code.py').st_mtime
print(datetime.fromtimestamp(mod_time))

print('\n')

# to see the entire directory tree and files within the desktop or it is used to do traversing(to go through all elements one by one)
for dirpath , dirnames , filenames in os.walk('/Users/m1-pro/Desktop'):# is a generator that yeilds a tuple of three values as its walking the directory tree so for each directory it sees it yeilds the directory path
    print('Current Path:' , dirpath)
    print('Directories:' , dirnames)
    print('Files:' , filenames)
    print()
    
# to access home directory

print(os.environ)# it will print all the environment variables
print(os.environ.get('HOME')) 

# to create a new file within my home directory 
'test.txt'

# Bad method to combine new file 'test.txt' with home directory
file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)

# to combine properly this 'test.txt' file with home directory
file_path = os.path.join(os.environ.get('HOME') , 'test.txt')
print(file_path)

# to grab the file name of any path were working on, and this doesn't have to be a real path
print(os.path.basename('/tmp/test.txt'))

# to want only directory name
print(os.path.dirname('/tmp/test.txt'))

# want to print both directory and file name we can do this:
print(os.path.split('/tmp/test.txt'))

# to check if path exist originally on file system
print(os.path.exists('/tmp/test.txt'))

# to check if something is directory or file 
"""For directory"""
print(os.path.isdir('/tmp/fgfgggdgd'))
"""For File"""
print(os.path.isfile('/tmp/fgfgggdgd'))

# to split the file root and extension with slash
print(os.path.splitext('/tmp/test.txt'))


print('\n')

print(dir(os.path))
