# #arithmetic operators
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # remainder
print(a ** b) # a^b 

#relational operators
a = 50
b = 100

print(a == b) #False(Equal to)
print(a != b) #True(Not Equal to)
print(a >= b) #False(Greater than or Equal to)
print(a > b) #False(Greater than)
print(a <= b) #True(Less than or Equal to)
print(a < b) #True(Less than)

#assignment operators
num = 10
num = num + 10 #10+10 => 20
num += 10 #Both statements are same
num *= 5
print("num : ", num)

#logical operators
#not
print(not False)
print(not True)

a = 50
b = 100
print(not False)
print(not (a > b))

#and
val1 = True
val2 = True
print("and operator:", val1 and val2)

val3 = True
val4 = False
print("and operator:", val3 and val4)

#or
print("or operator:", val1 or val2)
print("or operator:", val3 or val4)

print("or operator:", (a == b) or (a > b)) 

#Input
name = input("Enter your name: ")
print("Hello", name)

val = input("Enter some value: ")
print(type(val), val) # "25", "99.99"

#input function always works on str
#to make it input integers we'll use type casting

val1 = int(input("Enter a value: "))
print(type(val1), val1)

name1 =  input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks: "))

print("Welcome", name1)
print("age =", age)
print("marks =", marks)

#Type conversion
a = 5 #integer
b = 4.25 #float

sum = a + b #it will automatically convert integer to float
print(sum) # 5.00 + 4.25 => 9.25

#Type casting
c = float("5")
d = 4.25

print(type(c))
print(c + d)

e = 3.14
e = str(a)

print(type(e))