#WAF(Write a Function) to print the length of a list.(list is the parameter)
cities = ["delhi", "raipur", "noida", "mumbai", "pune", "chennai"]
heroes = ["thor", "ironman", "hulk", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


#WAF to print the elements of a list in a single line.(list is parameter)
cities = ["delhi", "raipur", "noida", "mumbai", "pune", "chennai"]
heroes = ["thor", "ironman", "hulk", "shaktiman"]

print(heroes[0], end = "\n")
print(heroes[1], end = "\n") #...and so on

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(cities)
print_list(heroes)


#WAF to find the factorial of n.(n is the parameter)
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

def cal_falc(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

cal_falc(6)

#WAF to convert USD to INR.
curr = 1
def usd_to_r(curr):
    print(curr, "USD =", curr * 80, "INR")

usd_to_r(2) 

#WAF to input a number, if the number is odd then print "ODD", if even print "EVEN"
x = int(input("Enter your number:" ))
def even_odd(x):
    if (x % 2 == 0) :
        print("Even")
    else :
        print("Odd")

even_odd(x)


#Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_n (y):
    if y == 1:
        return 1
    else:
        return sum_of_n(y-1) + y 

inp = int(input("Enter a number : "))
print("Sum of first", inp, "is equal to", sum_of_n(inp))

#Write a recursive function to print all elements in a list.
#Hint : use list & index as parameters.(list, idx)
def print_list(list, idx = 0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

browser = ["chrome", "edge", "firefox", "brave"]
print_list(browser)