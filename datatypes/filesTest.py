# f = open("myfile.txt", "x")

f = open("myfile.txt", "a")
f.write("Hi! This is my content! \n")
f.close()

# open and read the file after the overwriting:
f = open("myfile.txt", "r")

print("File content : ", f.read())
content = f.read()  # Doesn't work as the cursor is already at the end of the line.
print("Content : ", content)
f.seek(0)  # Resetting the cursor
content = f.read()  # Works
print("Content : ", content)

f.seek(0)
print("Reading lines as list : ", f.readlines())

# This operation closes the files automatically, no need to close the file explicitly
with open('myfile.txt', mode="r") as f:
    contents = f.read()
    print("Reading it with style : ", contents)

# print(f.read()) - This will generate error at this position, as the file is already closed.

# Modes
# mode='r' is read only
# mode='w' is write only (will overwrite files or create new!)
# mode='a' is append only (will add on files)
# mode='r+' is reading and writing
# mode='w+' is writing and reading (Overwrites existing files or creates a new file!)


# "x" - Create - will create a file, returns an error if the file exist
#
# "a" - Append - will create a file if the specified file does not exist
#
# "w" - Write - will create a file if the specified file does not exist


