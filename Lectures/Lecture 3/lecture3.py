#Lists in python(To store buil-in data)
m1 = 94.5
m2 = 67.7
m3 = 34.6
m4 = 97.5
m5 = 86.5
#To avoid so much variable we use list
marks = [94.5, 67.7, 34.6, 97.5, 86.5] #List
print(marks)
print(type(marks))
#Indexing in Lists
print(marks[0])
print(marks[1])
print(len(marks)) #Length of Marks List = 5
#Storing str, int, float etc
student = ["Advik", 93.5, 18, "Chhattisgarh" ] #Py List can store str, int, float etc in a single list, in this example it is student = [name, marks, age, location]
print(student)

#Strings are immutable(cannot be changed) but Lists are mutable(can be changed) in Py, means we can access and change the value in the list but not in the string while indexing.
str = "namaste"
print(str[0])
# str[0] = "y" --> This is not valid in string(Immutable)
print(student[0])
student[0] = "Bruno" #This is valid in list(Mutable)
print(student)
# print(student[5]) --> This will give an error as there is nothing included in the student list

#List Slicing - list_name[ starting_idx : ending_idx], ending_idx is not included
marks = [94.5, 67.7, 34.6, 97.5, 86.5]
print(marks[1:4]) #Sublist

print(marks[0:4]) #Sublist
print(marks[:4]) #Both statement will give same output

print(marks[1:]) #Sublist
print(marks[1:len(marks)]) #Both statement will give same output
print(marks[-4:-1]) #Negative indexing(slicing)


#List methods
list = [3, 2, 4]
list.append(5) #adds one element(5) at the end of list[3, 2, 4, 5]
print(list) #also known as mutating the list(change)

print(list.sort())
list.sort() #arranges the list in ascending order
print(list)

list.sort(reverse = True) #arranges the list in descending order
print(list)

#These methods are also applicable if the input in list are str
list1 = ['Litchi', 'Apple', 'Banana', 'Watermelon']
list1.append('Kiwi') #adds kiwi at the end
print(list1)
list1.sort() #arranges the list based on dictionary
print(list1)
list1.sort(reverse = True) #arrange in descending order
print(list1)

#Another example {listname.reverse()}
list2 = ['a', 'd', 'e', 'f', 'c', 'b']
list2.reverse()
print(list2) #Use list.reverse in beginning if you ever want to use

#To insert an element at index
list = [3, 2, 4]
list.insert(1,5) #list.insert(idx, element)
print(list) #adds 5 after 0th index or 5 takes 1st index

#To remove something
list3 = [2, 1, 3, 1]
list3.remove(1)
print(list3) #Removes first occurence of '1'
list3.pop(2)
print(list3) #Removes all 2'


#Tuples in python(Built-in data type which are not immutable)
#Tuples works almost like Lists
tup = (50, 52, 54, 56)
print(type(tup))
print(tup[0]) #Prints 50
print(tup[1]) #Prints 52
#tup[0] = 48 will create an error as tuples are immutables like str

tup1 = () #valid tuple
print(type(tup1))
print(tup1)

#For a single element tuple, we will seperate it with (,) otherwise the class would not be a tuple it will become int, str or float.
tup2 = (1,)
print(type(tup2))
print(tup2)

#For multiple values we can separate it with commas, it's on our own
tup3 = (1, 2, 3, 4) #or we can write(1, 2, 3, 4,)
print(type(tup3))
print(tup3)
#Tuple Slicing
print(tup3[1:3])

#Tuple Methods
tup4 = (2, 1, 3, 1)
print(tup4.index(1)) #returns index of first occurence
print(tup4.count(1)) #counts total occurrences

## End of Lecture ##
