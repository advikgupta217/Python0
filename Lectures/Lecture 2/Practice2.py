#WAP to input user's first name & print it's length
Name = input("Enter your first name : ")
print("Length of your name is :", len(Name))


#WAP to find the occurrence of "$" in a string
Sentence = input("Enter your sentence :" )
print(Sentence.count("$"))


#WAP to check if a number entered by the user is even or odd
num = int(input("Enter a number : " ))
if(num % 2 == 0):
    print("Your number is divisible by 2")
else:
    print("Your number is not divisible by 2")


#WAP to find the greatest of 3 numbers entered by the user
x = int(input("Enter your first number : " ))
y = int(input("Enter your second number : " ))
z = int(input("Enter your third number : " ))

if(x > y > z) or (x > z > y):
    print("Greatest number is :", x)
if(y > x > z) or (y > z > x):
    print("Greatest number is :", y)
if(z > x > y) or (z > y > x):
    print("Greatest number is :", z)


#WAP to check if a number is multiple of 7 or not
num2 = int(input("Enter your number : " ))
if(num2 % 7 == 0):
    print("Your number is a multiple of 7")
else:
    print("Your number is not a multiple of 7")

