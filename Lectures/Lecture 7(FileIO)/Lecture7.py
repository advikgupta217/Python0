# #File Input/Output in Python-Used to perform operations on a file(Read & Write data)
# → We have to open a file before reading or writing

# f = open("file_name", "mode")

# data = f.read()
# f.close()

# → file name - sample.txt or demo.docx
# → mode - r:read mode, w:write mode,(default mode for python is r)

f = open("demo.txt", "r") #we can also write "rt" instead or "r".
data = f.read()
print(data)
print(type(data))
f.close()

# ▪ Modes
# 	→ 'r' - open for reading(default)
# 	→ 'w' - open for writing, truncating the file first
# 	→ 'x' - create a new file and open it for writing
# 	→ 'a' - open for writing, appending to the end of the file if it exists
# 	→ 'b' - binary mode
# 	→ 't' - text mode(default)
#   → '+' - open a disk file for updating(reading and writing)
f = open("demo.txt", "r") #we can also write "rt" instead or "r".
# data1 = f.read(10) #prints 1st ten letters of document
# print(data1)
# print(type(data1))

line1 = f.readline() #prints a line
print(line1)

line2 = f.readline() #prints a line
print(line2)

line3 = f.readline() #prints empty line
print(line3)

f.close()

#Writing to a file
f = open("Ad.txt", "w")
f.write("I will conquer the world of coding")
f.close()

#Append
f = open("demo1.txt", "a")
f.write("\n I am learning Python") #adds new data in next line due to \n
f.close()

#In a/w mode, python automatically adds a new file, if not there.
f = open("sample.txt", "w")
f.close() #creates a new file

#Combining modes
# r+ : Overwrites a file from beginning
f = open("demo1.txt", "r+")
f.write("abc")
print(f.read())
f.close()

# w+ : File is truncated 
f = open("demo2.txt", "w+") #File is deleted and it prints "abc"
f.write("abc")
print(f.read())
f.close()

# a+ : Appends from the End

#with Syntax
# with open("demo.txt", "a")as f:
#    data = f.read()
with open('demo3.txt', "r") as f:
    data1 = f.read()
    print = data1

with open("demo3.txt", "w") as f:
    f.write("New data")

#Deleting a file
# Using the os module
# Module is a file written by another programmer that generally has a functions we can use.

import os
os.remove("sample1.txt")

##End of Lecture##