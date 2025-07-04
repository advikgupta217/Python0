## Lecture 8.2 ##

#del Keyword - Used to delete object properties or object itself.
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Advik")

del s1
# print(s1) - As s1 is deleted this will show an error

#Private(like) attributes & methods - Meant to be used only within the class and are not accessible from outside the class.
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no #This can be public
        self.acc_pass = acc_pass #This data has to private

acc1 = Account("2124", "Advik@123")

print(acc1.acc_no)
print(acc1.acc_pass) #This has to be private, For sensitive information we'll use private attribute(double underscore).
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no #This can be public
        self.__acc_pass = acc_pass #This data has to private
    def reset_pass(self):
        print(self.__acc_pass) #This will work as it is inside the class

acc1 = Account("2124", "Advik@123")

print(acc1.acc_no)
print(acc1.reset_pass())
# print(acc1.__acc_pass) - This will print error

class Person:
    __name = "anonymous" # we made it private

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello() #This function internally calls hello function

p1 = Person()

# print(p1.name)- This will again be an error
# print(p1.__hello())- error
print(p1.welcome())


#Inheritance - When one class(child/derived) derives the properties & methods of another class(parent/base). To inherit something from an old class.
#Single inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start()) #As we have used inheritance therefore there will be no error
print(car1.color)

#Multi-level inheritance
class Car:
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car): #This will inherit properties from Car class
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar): #This will inherit properties from ToyotaCar class
    def __init__(self, type):
        self.type = type
    
car3 = Fortuner("diesel")
car1.start() #In Car class

#Multiple Inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


#Super method - Used to access methods of parent class.
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car): #This will inherit properties from Car class
    def __init__(self, name, type):
        self.name = name
        super().__init__(type) #super constructor
        super().start()
    
car4 = ToyotaCar("prius", "electric")
print(car4.type)

#Class method - Bound to the class & recieves the class as an implicit first argument. 
#Note - Static method can't access or modify class state & generally for utility.

class Person:
    name = "Anonymous"

    #def changeName(self, name):
        #Person.name = name - Person.name will change the class attribute orwe can use self.__class__.name = "Advik"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Advik Gupta")
print(p1.name)
print(Person.name)

#Property decorator - To use the method as property

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str ((self.phy + self.chem + self.math) / 3) + "%"

    def calcPercentage(self):
        self.percentage = str ((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86 #Supposed to be 86
print(stu1.phy) #percentage won't change automatically
stu1.calcPercentage()
print(stu1.percentage)


#Polymorphism : Operator overloading - When the same operator is allowed to have different meaning according to the context.

print(1 + 2) #3
print("Advik" + "Gupta") #concatenate
print([1, 2, 3] + [4, 5, 6]) #merge 
#All these forms of + is known as Operator overloading (Implicit), as it is different for integer, string, list etc.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(2, 3)
num1.showNumber()

num2 = Complex(3, 4)
num2.showNumber()
#Now if we want to add these complex numbers, we'll use Dunder functions(Operator overloading) __add__
num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()