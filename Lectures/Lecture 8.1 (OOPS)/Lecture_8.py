#Object Oriented Programming(OOP) - To map with real world scenarios, we started using objects in code
a = 10
b = 20 

sum = a + b
print(sum)

diff = a - b
print(diff) 
#This is Procedural Programming(step by step)
#Functions were used to reduce redundancy and increase reusability.
#One step further is OOP(Objects and Classes)

#Class & Object in Python
#Class is a blue print for creating objects
class Student: #Creating class
    name = "Advik Gupta"

s1 = Student()  #Creating Object(instance)
print(s1.name)

s2 = Student() #Objects are made from class
print(s2.name)

#Factory for a car
class Car:
    color = "blue"
    brand = "audi"

car1 = Car()
print(car1.color)
print(car1.brand)

#__init__ Function
# → Constructor : All classes have a function called __init__(), which is always executed when object is being initiated.(New objects are created)

#Creating class
class Student:
    def __init__(self, fullname):
        self.name = fullname 

#Creating object
s1 = Student("Advik") #Creates a new object 
print(s1.name)

#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

class Student: 
    name = "Advik"
    def __init__(self): #Constructor always uses a parameter(self)
        print("Adding new student in database..")
        print(self)

s1 = Student() #() are used to call the instructor
print(s1)

#If we want to assign different names to different students
class Student:
    #Default constructor
    def __init__(self): #self is always 1st parameter 
        pass
    #Parametrized constructor
    college_name = "IIT Dholakpur"
    def __init__(self, name, marks): #We'll add another parameter
        self.name = name #Store "name" in s1.name, s2.name ...etc
        self.marks = marks
        print("Adding new student in database..")

s3 = Student("Bruno", 100) #() are used to call the instructor
print(s3.name, s3.marks)

s4 = Student("Arjun", 98)
print(s4.name, s4.marks)

print(s3.college_name)
print(s4.college_name)

#Class & Instance Attributes - Data or Variable(name, marks etc)
#For e.g if we create a class named Student and add s1, s2, s3 and s4(objects), we know for sure that all have different names(name), then the name would be an instance attribute (har object ka alag hoga) it would be defined by self.name(.name), similarly it is with marks, self.marks(.marks). But if we talk about School name or College name it would be common for all s1, s2, s3, s4, therefore it would be a Class attribute which would be common for all the objects made inside the class and will be defined as college_name = "ABC College" succeding the constructor. Class attr. is stored in memory only a single time as it is common for all and on the other hand instance attr. are stored different for different objects in this case name and marks.

#If we want to assign different names to different students(without any comments interuppting)
class Student:
    
    college_name = "IIT Dholakpur" #Class attr.
    def __init__(self, name, marks):
        self.name = name  #Instance attr.
        self.marks = marks #Instance attr.
        print("Adding new student in database..")

s3 = Student("Bruno", 100)
print(s3.name, s3.marks)

s4 = Student("Arjun", 98)
print(s4.name, s4.marks)

print(s3.college_name)
print(s4.college_name)

#Jb bhi class attr. aur obj/instance attr. ki same value hoti hai tb obj attr. ko jyada preference milti hai.

#Methods - Functions that belong to objects
#Class is a collection of two things - Data(Attributes) and Methods(Functions)
class Student:
    
    college_name = "IIT Dholakpur"
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
    
    def welcome(self): #Creating a new method/function
        print("Welcome student,", self.name)
    
    def get_marks(self):
        return self.marks

s3 = Student("Bruno", 100)
s3.welcome() #Calling our new method/function
print(s3.get_marks())


s4 = Student("Arjun", 98)
s4.welcome() #Calling our new method
print(s4.get_marks())

print(s3.college_name)
print(s4.college_name)

#Static methods(If we don't want to use self parameter) - Methods that don't use the self parameter(work at class level), self are used for objects

class Student:
    
    @staticmethod #decorator - class level
    def hello(): # No use of self parameter
        print("Hello")

    def __init__(self, name):
        self.name = name 

s3 = Student("Bruno")
print(s3.name)
s3.hello()

#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.(Changing behaviour of a normal function)

#Pillars of OOPS - Abstraction, Encapsulation, Inheritance and Polymorphism
#(1) Abstraction - Hiding the implementation details of a class and only showing the essential features to the user.(Hiding unnecessary feature from the user)
class Car:
    def __init__(self):
        self.acc = False #Accelerator is not pressed
        self.brk = False #Break is not pressed
        self.clutch = False #Clutch is not pressed

    def start(self):
        self.clutch = True #Clutch is pressed
        self.acc = True #Accelerator is pressed 
        print("Car started..")

car1 = Car() #Car1 object
car1.start() #Here acc, brk and clutch are unecessary for the driver therefore this is an abstraction

#(2) Encapsulation - Wrapping data and functions into a single unit/capsule(object), Capsule of data + related functions in a single unit.

## End of Lecture ##