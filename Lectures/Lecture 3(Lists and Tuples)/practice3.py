#WAP to ask the user to enter names of their 3 favorite movies & store them in a list
movie1 = input("Enter your 1st movie:" )
movie2 = input("Enter your 2nd movie:" )
movie3 = input("Enter your 3rd movie:" )
list = [movie1, movie2, movie3]
print("Your movies are", list)

#or

movies = []
mov1 = input("Enter your 1st movie:" )
mov2 = input("Enter your 2nd movie:" )
mov3 = input("Enter your 3rd movie:" )

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print("Your movies are", movies)


#WAP to check if a list contains a palindrome of elements. 
list = [1, 2, 3, 2, 1]
listcopy = list.copy()
listcopy.reverse()
#listcopy_reversed = listcopy.reverse() will not work, it will always print "Given list is not a palindrome"
if(listcopy == list):
    print("Given list is a palindrome")
else:
    print("Given list is not a palindrome")


#WAP to count the number of students with the "A" grade in the following tuple : ["C", "D", "A", "A", "B", "B", "A"]
#Store the above values in a list and sort them from "A" to "D"

tup = ("C", "D", "A", "A", "B", "B", "A")
count = tup.count("A")
print(count)

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print (grade)
