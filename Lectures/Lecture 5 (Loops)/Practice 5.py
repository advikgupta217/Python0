#Print numbers from 1 to 100
num = 1
while num <= 100 :
    print(num)
    num += 1


#Print numbers from 100 to 1
num1 = 100
while num1 >= 1 :
    print(num1)
    num1 -= 1


#Print the multiplication table of a number n
number = int(input("Enter your number: " ))
inputValue = int(input("Enter your range: " ))
num2 = 1
while num2 <= inputValue :
    print("Your multiplication table is ", number * num2)
    num2 += 1 


#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num3 = 1
while num3 <= 10 :
    print(num3 * num3)
    num3 += 1
#or
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


#Search for the number x in the tuple using loop: (Linear search)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0 #initialization
while i < len(tup):
    if(tup[i] == x):
        print("Found at index", i)
    else:
        print("Finding..")
    i += 1


#Using for, Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for sqr in list1:
    print(sqr)
print("")

#Search for a number y in this tuple using loop:(Linear search)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
y = 49
idx = 0

for el in list2:
    if(el == y):
        print("number found at idx", idx)
    idx += 1
print("")

#Using for & range() - Print numbers from 1 to 100
for i in range(1, 101):
    print(i)
print("")


#Using for & range() - Print numbers from 100 to 1
for i in range(101, 0, -1):
    print(i)


#Using for & range() - Print the multiplication table of a number n
n = int(input("Enter your number:" ))
for i in range(1,11):
    print (n * i)


#WAP to find the sum of first n numbers.(Using loops)
z = int(input("Enter a number: "))
i = 1
total = 0

while i <= z:
    total += i
    i += 1
print("Sum of first", n, "natural numbers is", total)

#Alternative

m = int(input("Enter a natural number: "))
sum = 0
for i in range(1, m+1):
    sum += i

print("Total sum =", sum)


#WAP to find the factorial of first n numbers.(Using loops)
facto = int(input("Enter value for factorial"))
facto1 = 1
i = 1
while i <= facto:
    facto1 *= i
    i += 1

print("Factorial =", facto1)

#Alternative(For)
fact = int(input("Value for factorial = "))
fact1 = 1
for i in range(1, n+1):
    fact1 *= i

print("Factorial =", fact1)