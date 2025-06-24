# Functions in Python → Block of statements that performs a specific task
# 		def func_name(param1, param2..)
# 			#some work
# 			return val
#
# 		func_name(arg1, arg2..) #function call
# We can use function wherever and whenever we need after defining what it should do, for eg

a = 5
b = 10
sum = a + b
print(sum)

#more lines of code
#again
a = 2
b = 10
sum = a + b
print(sum)

#some more lines of code
#again
a = 4
b = 3
sum = a + b
print(sum)

#To ignore this repeated steps(reduntant code) we use a function, 
#Redundant codes are signs of bad programmer(advised to convert it in a function), in this case,
def calc_sum(a, b):  #Inside () are parameters or inputs
    sum = a + b #work
    print(sum)
    return sum #output

#Now we can ignore all the above steps and we can CALL this f(x)
calc_sum(5, 10) #inside this (arguments) are stored in above parameters
calc_sum(2, 10) #functions are used to reduce redundancy
calc_sum(4, 3) #Less lines of code work is same

def print_hello():
    print("hello")

output = print_hello()
print_hello()
print_hello()
print_hello() #function call
print(output) #None

#Average of three numbers
def avg_three_num(a, b, c):
    avg = (a + b + c)//3
    print(avg)
    return avg #we can also apply all conditions(if, elif, else) and loops as well

avg_three_num(4,5,9)

print("Advik Gupta", end = " ") #hover in print it will show sep = ""
print("Coder") #end = "\n" ???, we have defined end = " "
#Some functions are already defined in Python are known as Built-in functions, and which are defined by us are known as User defined functions.

#Default parameters - Assigning a default value to a parameter, which is used when no argument is passed in func call:

# def cal_prod(a, b):
#     print(a * b)
#     return a * b

# cal_prod(), as there is no argument given, therefore it will give an error,so,we'll give our parameters a default value.
def cal_prod(a = 1, b = 1):
    print(a * b)
    return a * b

cal_prod()


#Recursion - When a function calls itself repeatedly.(Loops ka khatarnak version)
#Recursion and Loops are both interelated, both can perform same work, but we prefer anyone according to our preference.

# def show(n):
#     print(n)

# show(5) #5, 4 = n-1, 3 = n-2, 2 = n-3, 1 should be printed in 1 show call using recursion, therefore
#prints n to 1 backwards
def show(n):
    if (n == 0): #Base case is important in recursion
        return
    print(n)
    show(n-1) #This will again take input in show()
    print("END")
show(3)

#returns n! 
def fact(n): #n! = (n-1)! x n
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(4))

## End of lecture ##