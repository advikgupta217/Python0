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

acc1 = Account(10000, 21270709)
print("Your account balance is : ",acc1.balance)
print("Your account no. is : ",acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(200000)
acc1.debit(30000)