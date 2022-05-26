#The append() method appends an element to the  end array
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)




#Remove all the elements from the fruits List:
#syntax: list.clear()
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

#The copy () method returns a copy of the specified list.
#Copy the fruits list:
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)


##the count() method returns the number of elements with the specified value
#systax: list.count(value)
#Return the number of times the value "cherry" appears in the fruits list":
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cheery")
y = len(fruits)
print(x)
print(f"Total length of fruits array is {y}")


#Write a program to ask the numbers of users
#add the names by user input
#ask the user to search any names
#if found give result "Search {realName} Found"
number = int(input("How many names you want to add:"))
names=[]
for i in range(number):
    name = input("Enter the Name:")
    names.append(name)
print(names)
search = input("Enter the name for Search :")
count = names.count(search)
if count>=1:
    print(f"Search {search} Found")
else:
    print(f"Search {search} Not Found")

#Write a program to ask the numbers of user
number = int(input("How many numbers you want to add:"))
sum = 0;
average = 0
for i in range(number):
    num = int(input(f"Enter the number {i}:"))
    sum = sum+num
average = float(sum/number)
print(f"The Sum is {sum}")
print(f"The average is {average}")

# Find the greatest Number
# Find the Smallest Number






#The  extend() method adds the specified list elements (or any iterable)to the end of the current list.
#Syntax: list.extend(iterable)
#add the elements of cars to the fruits list:
fruits = ['apple','banana', 'cherry']
cars = ['ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#The index() method returns the position at the first occurrence of the specified value.
# Syntax: list.index(elmnt)
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#The insert() method inserts the specified value at the specific position.
#syntax list.insert(pos, elmnt)
#pos: Required. a number specifying in which position to insert the value
#elmnt : Required, An element of any type (string, number, object etc.)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1,'orange')
print(fruits)

#the reverse() method






#The sort() method sorts the list ascending by default.
#you can also make a function to decide the sorting criteria(s).
#syntax: list.sort(reverse=True/False, key=myFunc)
cars = ['Ford','bmw','volvo']
cars.sort(reverse=True)
print(cars)

#a function that returns the length of the value:
def myFunc(e):
    return len(e)
cars = ['ford','mitsubishi','bmw','vw']
cars.sort(key=myFunc)
print(cars)











