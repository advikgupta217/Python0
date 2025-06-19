#Write a program to input 2 numbers and print their sum
first = int(input("first number : "))
second = int(input("second number : "))

print("sum =", first + second)

#Write a program to input side of a square & print it's area
side = int(input("side of square = "))

print("area =", side*side) #or use side**2, (side)^2


#Write a program to input 2 floating point numbers & print their average
a = float(input("a = "))
b = float(input("b = "))

print("your average =", (a+b)/2)


""" Write a program to input 2 int numbers, c and d
Print true if c is greater than or equal to d. If not print False. """

c = int(input("Enter c ="))
d = int(input("Enter d ="))

if(c >= d):
    print("True")
else:
    print("False")