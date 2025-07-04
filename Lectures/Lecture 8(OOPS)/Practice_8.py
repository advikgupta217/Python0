#Create student class that makes & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student :
    def __init__(self, name, marks): #We'll assume that marks will be in the form of list[x, y, z] 
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi!,", self.name, "Your avg score is:", sum/3)

s1 = Student("Advik Gupta", [98,99,100])
s1.get_avg()

s1.name = "Bruno"
s1.get_avg()


#Create Account class with 2 attributes - Balance & Account no. Create methods for debit(subtract), credit(add) & printing the balance.
class Account :
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.get_balance())

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance = ", self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 21240709)
print("Your account balance is : ",acc1.balance)
print("Your account no. is : ",acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(200000)
acc1.debit(30000)


#Define a Circle class to create a circle with radius r using the constructor. Define Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(14)
print(c1.area())
print(c1.perimeter())


#Define an Employee class with attributes role, department & salary. This class also has a showDetails() method. Create an Engineer class that inherits properties from Employee & has additional attributes : name & age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "CS", "100000")

e1 = Employee("accountant", "Finance", "50,000")
e1.showDetails()

engg1 = Engineer("Sundar Pichai", 45)
engg1.showDetails()


#Create a class called Order which stores items & its price. Use dunder function __gt__() to convey that: order1 > order2 if price of order1 > price of order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = Order("Lays", 20)
odr2 = Order("Pen", 10)

print(odr1 > odr2)