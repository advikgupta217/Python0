##Lecture 4
#Dictionary in Python (dict{}) key --> value
info = {
    "key" : "value", #str
    "name" : "Advik Gupta", #str
    "subjects" : ["python", "C", "Java"], #List
    "topics" : ("dict", "set"), #Tuple
    "learning" : "Python" , #str
    "age" : 18, #Integer
    "is_adult" : True , #Boolean
    "marks" : 93.5 #Float
}

print(type(info))
print(info) #All these values are acceptable in dictionary

#To print individual keys
print(info["key"])
print(info["name"])
print(info["subjects"])
print(info["topics"])
print(info["learning"])
print(info["age"])
print(info["is_adult"])
print(info["marks"])
#This will print accessable values from the dictionary 'info'
#print(info["surname"]), as surname does not exists as key in dictionary therefore this will create an error

#To assign someone something else
info["name"] = "Bruno" #overwrite
info["surname"] = "Gupta" #This will add a new key/value pair
print(info)

#Empty Dictionary
null_dict = {}
null_dict["name"] = "Advik Gupta"
print(null_dict)

#Nested Dictionaries (Dictionary within a Dictionary)
student = {
    "Name" : "Advik Gupta",
    "Subjects" : {
        "Physics" : 97,
        "Chemistry" : 98,  #We can assign a value to a dictionary
        "Mathematics" : 100
    }
}

print(student)
#We can also print marks for individual subjects
print(student["Subjects"]["Physics"])
print(student["Subjects"]["Chemistry"])
print(student["Subjects"]["Mathematics"])

# #Dictionary methods(dict)
# 	→ dict .keys()  #returns all keys
# 	→ dict .values()  #returns all values
# 	→ dict .items()  #returns all(key, val) pairs as tuples
# 	→ dict .get()  #returns the key according to value
#   → dict .update(newDict)  #inserts the specified items to the dictionary
student = {
    "Name" : "Advik Gupta",
    "Subjects" : {
        "Physics" : 97,
        "Chemistry" : 98,  #We can assign a value to a dictionary
        "Mathematics" : 100
    }
}

print(student.keys()) #returns all keys in student dictionary
print(list(student.keys())) #typecasted to list
print(len(student)) #returns the length of dictionary
print(len(list(student.keys()))) #returns the length of list made earlier

print(student.values()) #returns all values in student dictionary
print(list(student.values())) #typecasted to list

print(student.items()) #returns all key,value pairs as tuples
print(list(student.items())) #typecasted to list(Tuples within a list)
pairs = list(student.items())
print(pairs[0]) #1st tuple of the list
print(pairs[1]) #2nd tuple of the list

print(student["Name"])
print(student.get("Name")) #Both will give same results
# #But
# print(student["name2"]) #This will give an error
# print(student.get("name2")) #This will print None

new_dict = {"City" : "Dhamtari", "Age" : "18"}
student.update(new_dict)
print(student) #This function can also overwrite an existing key

#Set in python{1,2,3,4} - Collection of unordered items, each element in the set must be unique & immutable(cannot be changed)
collection = {1, 2, 3, 4, "hello", "world"}
print(type(collection))
print(collection) #Order doesn't matter in a set

collection1 = {1, 2, 2, 3, 4, "hello", "world", "world"}
print(type(collection1))
print(len(collection1))
print(collection1) #**In this case set ignores duplicate items**

#Null set
#collection = {} --> This is an empty dictionary not an Null set
collection2 = set() #This is a Null/Empty set
print(type(collection2))
print(collection2)

#Set Methods
	# → set.add(el)   #adds an element
	# → set.remove(el)   #removes the element
	# → set.clear()   #empties the set
    # → set.pop()   #removes a random value

collection3 = set() #Null set
collection3.add(1) #int(Immutable)
collection3.add(2) #int(Immutable)
collection3.add(2) #duplicate value(ignored)
collection3.add("Advik Gupta") #str(Immutable)
collection3.add((1, 2, 3)) #Tuple(Immutable)
collection3.add(True) #Boolean(Immutable)

#collection3.add([1, 2, 3]) # Error as List are mutable same will be followed in dictionary as it is also mutable

collection3.remove(1) #removes 1
#collection3.remove(7)  #Error as 7 does not exists in collection3
print(len(collection3))
print(collection3)

#If we want to clear any set
collection4 = set() #Null set
collection4.add(1) #int(Immutable)
collection4.add(2) #int(Immutable)
collection4.add(2) #duplicate value(ignored)
collection4.clear()
print(collection4)
print(len(collection4))

#Pop Method(To remove an element)
collection5 = {"Python", "C", "C++", "C#", "Java", "Hello"}
print(collection5.pop()) #Any element can be popped
print(collection5.pop()) #Python picks element randomly to pop
print(collection5.pop())

#Union method
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2)) #{1, 2, 3, 4, 5}
print(set1)
print(set2) #origin values will be retained

#Intersection method
print(set1.intersection(set2)) #{3}

## End of Lecture ##