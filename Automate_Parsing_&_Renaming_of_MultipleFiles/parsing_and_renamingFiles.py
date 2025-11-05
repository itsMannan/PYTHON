import os

# to change my directory which coontains all my files
os.chdir('/Users/m1-pro/Downloads/Videos')

"""print(os.getcwd())""" # to check if we are in the correct directory or not

# to list everything in directory
for f in os.listdir():
    print(f)
    
# to split of the extension from the file name
for F in os.listdir():
    print(os.path.splitext(F)) # it will give us a tuple in which first part is carrying the name like ('Sun') and second part is carrying the extension like ('.mp4')
    
for f in os.listdir():
    file_name, file_extension = os.path.splitext(f)
    print(file_name)
    """print(file_extension)"""
    
for f in os.listdir():
    file_name, file_extension = os.path.splitext(f)
    print(file_name.split("-")) # it will give us a list by spliting with hyphens
    
for f in os.listdir():
    file_name, file_extension = os.path.splitext(f)
    f_title , f_num = file_name.split('-')
    print(f_num)
    
# to print a formatted string
for f in os.listdir():
    f_name , f_ext = os.path.splitext(f)
    f_title , f_num = f_name.split('-')
    f_title =  f_title.strip() # Remove the white space on left and right
    f_num  = f_num.strip() # Remove the white space on left and right
    print(f'{f_num}-{f_title}{f_ext}')
    
print('\n')
  
for f in os.listdir():
    f_name , f_ext = os.path.splitext(f)
    f_title , f_num = f_name.split('-')
    f_title =  f_title.strip() # Remove the white space on left and right
    f_num  = f_num.strip()[1:] # Remove the white space on left and right
    print(f'{f_num}-{f_title}{f_ext}')
    
# To do a zero padded string there's a method for it called zfill
for f in os.listdir():
    f_name , f_ext = os.path.splitext(f)
    f_title , f_num = f_name.split('-')
    f_title =  f_title.strip() # Remove the white space on left and right
    f_num  = f_num.strip()[1:].zfill(2) # Remove the white space on left and right / Zfill to covert 1 into 01 and two means if there comes 10 it won't change it but if it is 2 or 3 it will add zero before them
    print(f'{f_num}-{f_title}{f_ext}')
    
print('\n')

for f in os.listdir():
    f_name , f_ext = os.path.splitext(f)
    f_title , f_num = f_name.split('-')
    f_title =  f_title.strip() # Remove the white space on left and right
    f_num  = f_num.strip()[1:].zfill(2) # Remove the white space on left and right / Zfill to covert 1 into 01 and two means if there comes 10 it won't change it but if it is 2 or 3 it will add zero before them
    new_name = f'{f_num}-{f_title}{f_ext}'
    
    os.rename(f , new_name)