#Create a new file "practice.txt" using python. Add the following data in it:
#Hi everyone we are learning File I/O using Java. I like programming in Java.
f = open("practice.txt", "w")
f.write("Hi everyone\nwe are learning File I/O\n")
f.write("using Java.\nI like programming in Java.")



#WAF that replace all occurrences of "Java" with "Python" in above file
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

#Overwrite
with open("practice.txt", "w") as f:
    f.write(new_data)


#Search if the word "learning" exists in the file or not.
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(word in data):
        print("Found")
    else:
        print("Not found")


#WAF to find in which line of the file does the word "learning" occurs first. Print -1 if word not found.

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1

    return(-1)

check_for_line()
