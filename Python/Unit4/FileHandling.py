# Checking if the file is opened or not
fileptr = open("file.txt", "r")
if fileptr:
    print("File is opened successfully!")
fileptr.close()

# Reading the file
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# Writing onto the file
fileptr1 = open("file.txt", "w")
fileptr1.write("Hey!, how are you?")
fileptr1.close()

# Printing the lines of the file
fileptr = open("file.txt", "r")
for i in fileptr:
    print(i)

# Readline method
fileptr = open("file.txt", "r")
content = fileptr.readline()
content1 = fileptr.readline()
print(content)
print("Just printed line in variable content")
print(content1)
fileptr.close()

# Readlines method
fileptr = open("file.txt", "r")
content = fileptr.readlines()
print(content)
fileptr.close()

# Tell method
fileptr = open("file.txt", "r")
print("The filepointer is at byte:", fileptr.tell())
content = fileptr.read()
print("After reading the filepointer is at: ", fileptr.tell())

fileptr = open("file.txt", "r")
content = fileptr.readline()
content1 = fileptr.readline()
print(content)
print("Just printed line in variable content", fileptr.tell())
print(content1)
fileptr.close()

# Seek Method
fileptr = open("file.txt", "r")
print("The filepointer is at byte:", fileptr.tell())
fileptr.seek(10)
print("After reading the filepointer is at: ", fileptr.tell())
