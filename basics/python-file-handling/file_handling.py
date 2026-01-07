"""
File handling is a fundamental concept in Python.
This script demonstrates reading, writing, copying,
and working with text and binary files using best practices.
"""

# Opening a file By context managers
# Read mode
f = open('temporary.txt')  # open method specifly to takes a mode that wheather it has read,write,append.
print(f.mode)              # But by default it contains the read mode.

f.close()                  # When ever we open a file after completion of the work we should particularly close the file.

f = open('temporary.txt','r')
print(f.name)
print(f.mode)

f.close()

# Insted of explicitly closing a file we can close the file automatically by using  with context manager
with open('temporary.txt','r') as f:
    pass

print(f.mode)              # Here we not need to bother about the closing the file


# Reading the contents
# Methods
with open('temporary.txt','r') as f:
    f_contents = f.read()
    print(f_contents)

with open('temporary.txt','r') as f:
    f_contents = f.readlines()
    print(f_contents)

with open('temporary.txt','r') as f:
    f_contents = f.readline()
    print(f_contents)

with open('temporary.txt','r') as f:
    for line in f:
       print(line,end=" ")

# To have more control
with open('temporary.txt','r') as f:
     
     f_contents = f.read(100)          # reads first 100 characters
     print(f_contents,end=' ')

     f_contents = f.read(100)  
     print(f_contents,end='\n')
    
# This method can be used for the large files to read the specific type of content
with open('temporary.txt','r') as f:
    size_to_read = 30                       # Here after every 30 characters it will print in a new line.
    f_contents = f.read(size_to_read)
    print(f.tell())                         #Tell method is used to tell where the current cursor is prsent in reading.
    while len(f_contents)>0:
        print(f_contents,end = '\n')
        f_contents = f.read(size_to_read)

# Seek method
with open('temporary.txt','r') as f:
     size_to_read = 10
     f_contents = f.read(size_to_read)
     print(f_contents)
     f.seek(0)                               # Seek method is used to place the cursor in the specified position.
     f_contents = f.read(size_to_read)
     print(f_contents)
    
# Write Mode
with open('temporary_copy.txt','w') as wf:
        wf.write("Hello")                   # To enter the data into a file by writing the file should be open in the write mode
        wf.seek(0)
        wf.write('A')

# Copying the contents of one file to another file
with open('temporary.txt','r') as rf:
   with open('temporary_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

# Copying a picture from one file to another file
# To have more control we use this method 
with open('photo.jpg','rb') as pf:
    with open("photo_copy.jpg",'wb') as pcf:
        size_to_read = 4096
        f_contents = pf.read(size_to_read)
        while len(f_contents) >0:
            pcf.write(f_contents)
            f_contents = pf.read(size_to_read)

# Normal way to copy a picture from one file to another
with open('photo.jpg','rb') as pf:
    with open("photo_copy.jpg",'wb') as pcf:
        for line in pf:
            pcf.write(line)
