#All you have to do is type return "hello edabit.com"
def hello():
    return "hello edabit.com"


#Write a function that converts hours into seconds.
def how_many_seconds(hours):
	how_many_seconds = hours*60*60
	return(how_many_seconds)
print(how_many_seconds(2))


#Create a funciton that finds the maximum range of a triangle's third edge, where the side lengths are all integers
def next_edge(side1, side2):
	side3 = (side1 + side2) - 1  #Maximum length of the 3rd side is (side1 + side2) - 1
	return side3

#Write a function that takes the base and height of a triangle and return its area.
def tri_area(base, height):
	area = (base*height)/2
	return area

#Create a function that takes two numbers as arguments and returns their sum.
def addition(a, b):
	return a + b

#Create a function that takes a number as an argument, increments the number by +1 and returns the result.
def addition(num):
	return num + 1

#Write a function that takes an integer minutes and converts it to seconds.
def convert(minutes):
	seconds = minutes * 60
	return seconds

#Return the Remainder from Two Numbers
def remainder(x, y):
	return x % y

#Create a function that takes a string and returns it as an integer.
def string_int(txt):
	return int(txt)   #Return type is integer

#Create a function that takes the age in years and returns the age in days.
def calc_age(age):
	return age * 365

#Create a function that takes length and width and finds the perimeter of a rectangle.
def find_perimeter(length, width):
	return 2*(length + width)

#Create a function that takes voltage and current and returns the calculated power.
def circuit_power(voltage, current):
	return voltage*current

#Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).
def sum_polygon(n):
	return (n-2) * 180

#Code Wars
"""(Q) If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0."""
def solution(number):
    if number < 0 :
        return 0
    
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
        	total += i
     
#return total

"""(Q)Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!". """
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in string_:
        if char not in vowels:
            result += char
            
"""(Q) Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces."""
def get_count(sentence):
    count = 0
    for char in sentence:
        if char in "aeiou":
            count += 1
    return count

#or 

def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels

"""The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.
To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.
Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category."""

def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap >= 7 :
            result.append("Senior")
        else:
            result.append("Open")        
    return result

#or

def openOrSenior(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res

"""In a small town the population is p0 = 1000 at the beginning of a year. 
The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?"""

def nb_year(p0, percent, aug, p):
    year = 0
    population = p0
    
    while population < p:
        population = population + population * (percent/100) + aug
        year += 1
        
    return year




        
        
    
    