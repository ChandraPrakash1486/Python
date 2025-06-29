# File: code.py
# Description: Demonstrates various file handling operations in Python.

import os  # Import the os module for file system operations (e.g., removing files).

# --- File Path ---
# Define the absolute path to the 'test_code.py' file that will be manipulated.
# Using an absolute path makes the code less portable.
file_path = "c:\\Users\\us\\GitHub\\Python\\Intermediate_Python\\File Handling\\File\\test_code.py"

# --- File Creation (Commented Out) ---
# Creating a file using 'x' mode (exclusive creation) is commented out here.
# This mode would raise a FileExistsError if the file already exists.
# with open(file_path,"x") as file:
#     file.write("#this was created by x mode")

# --- Write Mode ('w') ---
# Open the file in write mode ('w').
# If the file exists, its contents will be completely overwritten.
# If the file does not exist, a new file will be created.
with open(file_path, "w") as file:
    file.write("#this was created by w mode\n")
    # After this operation, test_code.py will only contain the content: #this was created by w mode

# --- Append Mode ('a') ---
# Open the file in append mode ('a').
# This mode adds new data to the end of the file without erasing existing content.
# If the file does not exist, a new file will be created.
with open(file_path, "a") as file:
    file.write("#Appending the code\n")
    file.write("print('Hello World')\n")
    file.write("print('\\n')\n")
    # After this, test_code.py will contain: 
    # #this was created by w mode
    # #Appending the code
    # print('Hello World')
    # print('\n')

# --- Composite Mode ('r+') ---
# Open the file in read and write mode ('r+').
# This mode allows reading and writing.
# The file pointer starts at the beginning of the file.
# Writing will overwrite existing content from the current file pointer position.
with open(file_path, "r+") as file:
    file.write("#This is a composite mode")  # Overwrites from the beginning of the file.
    print(file.read())  # Reads and prints the remaining content of the file.
    # After this operation, test_code.py will contain: 
    # #This is a composite modeated by w mode
    # #Appending the code
    # print('Hello World')
    # print('\n')

# --- File Deletion ---
# Delete the file using os.remove().
# This operation is permanent.
# Check if the file exists before deleting it.
if os.path.exists(file_path):
    os.remove(file_path)  # Deletes the file specified by file_path
    print(f"File: '{file_path}' has been deleted!")
else:
    print(f"File: '{file_path}' does not exists!")

# Check if the file exists after deletion.
print(os.path.exists(file_path))  # Output: False (the file has been deleted)
#The file is now gone

# --- End of File Operations ---

# --- Credit ---
# Notes and documentation created by: Bard (AI Model)
