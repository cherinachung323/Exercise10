import sys, glob, os
# This imports the glob, sys and os modules.
# A module in Python is a file containing Python definitions and statements.
# The glob module provides a function for making file lists from directory wildcard searches.
# It is a way to search for files in directories using patterns.
# The os module provides a way of using operating system-dependent functionality, e.g. interacting with file paths.
# The sys module provides access to some variables used or maintained by the Python interpreter
# and provides access to functions that interact with the interpreter.

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# The above code is checking the operating system on which the Python script is running
# It then sets the hdir variable to the path of the user's home directory based on the operating system.

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
# Pattern is a variable that holds a string.
# This string tells glob what kind of files we're looking for
# os.path.join() is a function in the os module used to concatenate one or more path components intelligently.
# This function inserts the correct path separator (/ on Unix/Linux/macOS or \ on Windows) between components.
# This means that you don't have to worry about the underlying operating system's file path conventions.
# hdir: This is a variable that represents a directory path to the home directory in this case.
# The * is a wildcard that matches any number of characters

# Step 5: Use the glob.glob() function to obtain the list of filenames
file_list = glob.glob(pattern)
# The purpose is to find and list all files in a specific directory that match a certain pattern
# glob.glob(pattern) is the function call that does the work.
# It looks in the specified path for any files that match the pattern
for file_name in file_list:
    print(file_name)
# This is a loop that goes through each item in file_list.
# Each item in file_list is a path to a file that matched the pattern.
# The line print(file_name) prints out each of these file paths.

# Step 6: Use os.path.getsize() to find each file's size
for file_name in file_list:
    size = os.path.getsize(file_name)
    print(f"{file_name}: {size} bytes")
# You can include: if os.path.isfile(file_path) to check if it's a file and not a directory
# for loop iterates over a sequence of items.
# Each time the loop runs, it takes the next file path from file_list and assigns it to the variable file_path.
# size = os.path.getsize(file_path):
# Inside the loop, for each file_path, this line calculates the size of the file.
# os.path.getsize() is a function from the os.path module.
# It takes a file path as input and returns the size of the file in bytes.
# The size of the file (in bytes) is then stored in the variable size.
# print() is a function that writes out text to the console - it is inside the loop
# Inside print(), there's an f-string, indicated by f before the opening quote.
# An f-string is a way in Python to include variables' contents directly inside a string.
# This allows you to concatenate what appears to be an integer with a string
# {file_path} and {size} inside the f-string are placeholders
# These get replaced with the values of file_path and size variables.

# Step 7: Add a test to only display files that are not zero length
# Step 8: Remove the leading directory name(s) from each filename before you print it using os.path.basename()
# I am using a for statement here to check every single file in my file_list
for file_name in file_list:
    if os.path.getsize(file_name) != 0:
        # Step 8: Use os.path.basename() to remove the leading directory name(s)
        base_name = os.path.basename(file_name)
        print(base_name)

# or to print basename AND file size:
for file_name in file_list:
    size = os.path.getsize(file_name)
    if size > 0:
        base_name = os.path.basename(file_name)
        print(f"{base_name}: {size} bytes")
# the loop runs as above
# the loop takes the next file from the list as it runs and within the loop
# os.path.getsize() is a function from the os.path module.
# It takes a file path as input and returns the size of the file in bytes.
# basename just takes the file name from the file path
# if statement - file size is checked as above with the size function
# then if the size is >0 the basename and size are printed out

