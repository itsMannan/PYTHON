# Reading and writing to Files

# use built-in open command to get a file
# if your working with files from different directories then you have to copy their path and add it in open command but our file is within the directory thats why we don't need to copy the full path we can simply add the name of the file
# Open command allow us to specify whether we want to open the file for {Reading , Writing , Appending or Reading and writing}
# If we don't specify anything it we use this command for reading by default
f = open('test.txt' , 'r') # for reading

"""f = open('test.txt' , 'w')""" # for writing

"""f = open('test.txt' , 'a')""" # for appending

"""f = open('test.txt' , 'r+')""" # For both reading and writing


print(f.name)
print(f.mode) # to check in which mode we are working in i.e (r , w , a , r+w)

f.close()


# Opening file using context manager 

with open('test.txt' , 'r') as f:
    """To read the contents from the files within the  context manager"""
    f_contents = f.read()
    print(f_contents)
    

# To print the lines within the file in  a list
with open('test.txt' , 'r') as f:
    file_content = f.readlines()
    print(file_content)
 
 
# To print the lines within a file one by one
with open('test.txt' , 'r') as f:
    file_content = f.readline()
    print(file_content , end='')
    
    file_content = f.readline()
    print(file_content , end='')
    
    file_content = f.readline()
    print(file_content , end='')
    
print('\n')
    
with open('test.txt' , 'r') as f:
    for lines in f:
        print(lines , end='')
        
print('\n')
    
with open('test.txt' , 'r') as f:
    """To read the contents from the files within the  context manager"""
    f_contents = f.read(100) # specifying the amount of data we want to read at a time by passing the size as an argument
    # This will print the first 100 characters of our file instead of printing the whole thing all at once
    print(f_contents)
    f_contents = f.read(100) # specifying the amount of data we want to read at a time by passing the size as an argument
    # This will print the first 100 characters of our file instead of printing the whole thing all at once
    print(f_contents)

print('\n')

# Going to use a technique in Order to read in a large file

with open('test.txt' , 'r') as f:
    
    size_to_read = 100

    f_content = f.read(size_to_read)
    
    while len(f_content) > 0:
        print(f_content , end = '')
        f_content = f.read(size_to_read)
        
print('\n')

with open('test.txt' , 'r') as f:
    
    size_to_read = 10

    f_content = f.read(size_to_read)
    
    while len(f_content) > 0:
        print(f_content , end = '*')
        f_content = f.read(size_to_read)
        

print('\n')

with open('test.txt' , 'r') as f:
    s_t_r = 10
    f_cont = f.read(s_t_r)
    print(f_cont , end='')
    
    f.seek(0)
    
    f_cont = f.read(s_t_r)
    print(f_cont , end='')
    
    
    print('\n')
    print(f.tell()) # returns the position in a file
    

# Writting to files

# it will also create a file automatically if it was not there , but if the file was already there or you using an already built file then it will overwrite the file
# if you want to save your self for overwriting in to a file then you will use append lower case a  to the file
with open('test2.txt' , 'w') as f:
    pass

"""with open('test2.txt' , 'w') as f:
    f.write('Test')
    f.seek(0) # with using this, the second test will overwrote the first one
    f.write('R')"""
    
with open('test.txt' , 'r') as rf: # rf reading files (original file)
    with open('test_copy.txt' , 'w') as wf: # writing files (copy of file)
        for line in rf:
            wf.write(line)
      
# one way of copying one image to another
"""
with open('Goku.jpg' , 'rb') as rf :
    with open('Goku_copy.jpg' , 'wb') as wf:
        for line in rf:
            wf.write(line)
"""
# The second way is this
with open("Goku.jpg" , 'rb') as rf:
    with open("Goku_copy2.jpg" , 'wb') as wf:
        chunk_size = 4096
        read_chunks = rf.read(chunk_size)
        while len(read_chunks) > 0:
            wf.write(read_chunks)
            read_chunks = rf.read(chunk_size)