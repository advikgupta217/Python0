# Store following word meanings in a python dictionary
    #table : "a piece of furniture", "list of facts & figures"
    #cat : "a small animal"

dict = {
    "Table" : ["A Piece of furniture", "List of Facts & Figures"],
    "Cat" : "A small animal"
}
print(dict)
print(type(dict))

#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
subject = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(type(subject))
print("Classroom required :", len(subject))


#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
empty_dict = {}
mark1 = int(input("Enter marks of Physics :" ))
empty_dict.update({"Physics" : mark1}) #New key value

mark2 = int(input("Enter marks of Chemistry :" ))
empty_dict.update({"Chemistry" : mark2}) #New key value

mark3 = int(input("Enter marks of Mathematics :" ))
empty_dict.update(({"Mathematics" : mark1})) #New key value

print(empty_dict)


#Figure out a way to store 9 & 9.0 as separate values in the set
#(You can take help of built-in data types) {9,9.0}

values = {9, 9.0}
print(values) #This only prints 9, as both have same hash value

values1 = {9, "9.0"}
print(values1)
#or
values2 = {"9.0", 9}
print(values2)
#or
value = {
    ("float", 9.0)
    ("int", 9)
}
print(value)