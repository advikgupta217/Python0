#Strings

str1 = "This is a string, we are creating it in python."
str2 = 'Advik Gupta'
str3 = """This is a string"""

#Escape sequence characters(Formatting)

str4 = "This is a string, \n we are creating it in python." # \n will change the line
str5 = "This is a string, \t we are creating it in python." # \t will give tab space
print(str4)
print(str5)

#Basic Operations - Concatenation
str6 = "Advik"
str7 = "Gupta"
final_str = str6 + str7
print(final_str) #Advik + Gupta = AdvikGupta

#Basic Operations - Length of String
len1 = len(str1)
print(len1)

len2 = len(str2)
print(len2)

#Indexing
str8 = "Advik Gupta"
ch = str8[0] #A
print(ch) # str8[5] = "@" is not possible (We cannot modify)

#Slicing(Accessing parts of a string)
str9 = "Advik Gupta"
ch1 = str9[1 : 5]
print(ch1) #dvik
print(str9[:5]) #Advik
print(str9[0:]) #Advik Gupta
print(str9[0:len(str9)]) #Advik Gupta

#Negative index
str10 = "Apple"
print(str10[-3:-1]) #pl
print(str10[-5:-2]) #App 

#String functions
str11 = "i am a Coder."
print(str11.endswith("er.")) #Checks if the string ends with er.
print(str11.endswith("er")) #False 

print(str11.capitalize()) #Capitalizes 1st letter of the word
print(str11) #It will not change or capitalize
#To print the original string
str12 = str11.capitalize() #Take a new string as a new variable
print(str12)

str13 = "Racecar"
print(str13.replace("c", "a")) #replaces all c's with a
print(str13.replace("car", "bike")) #replaces car with bike

str14 = "My favorite movie is @Interstellar."
print(str14.find("Interstellar.")) #returns first index of word Interstellar
print(str14.find("@")) #returns first index of @
print(str14.find("q")) #returns -1 as it is not there in str14

str15 = "I am learning Python from online learning "
print(str15.count("learning")) #counts how many times learning is written

#Conditional Statements(if-elif-else)
age = 21

if(age >= 18):
    print("Can vote & Apply for License")
    print("Can drive and can vote")

#Traffic light - Program for traffic light mechanism
light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("Light is broken")

print("end of code")

#Another example - Program to check if the number is greater than 2/3
num = 5

if(num > 2):
    print("greater than 2")
if(num > 3):
    print("greater than 3") #This will print 2 statements

num1 = 5

if(num1 > 2):
    print("greater than 2")
elif(num1 > 3):
    print("greater than 3") #This will only print one statement

#Another Example - Program for valid age for Driving/Voting

age1 = 24

if(age >= 18):
    print("Can drive and Vote") #Indentation {}
else:
    print("Cannot drive or vote")

#Grading system - Program for assigning Grade A,B,C or D based on marks

marks = int(input("Enter your marks", ))

if(marks >= 90):
    print("Grade A")
elif(90 > marks >= 80): #Or we can write elif(marks>=80 and marks<90)
    print("Grade B")
elif(80 > marks >= 70): #Or we can write elif(marks>=70 and marks<80)
    print("Grade C")
else:
    print("Grade D")

#Nesting(if within if) - Program to vote within the age of 18 to 80
age2 = int(input("Enter your age : ", ))

if(age2 >= 18):
    if(age2 >= 80):
        print("Cannot vote")
    else:
        print("Can vote")
else:
    print("Cannot vote")

 