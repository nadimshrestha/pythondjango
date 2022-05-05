print ("hello world")


if True:
    print ("Answer")
    print ("true")
else:
    print ("Answer")
    print ("False")
print("I am outside of the block")
#Multi-line Statements
#continuation character (\)
total = "item_one + \
item_two + \
item_three"
print (total)

#this is an example of multiline comments
#this is a comment
#This is a comment.too.
#this is a comment,too.
#multiline comments
'''this is multiline'''


#multiple statements on a single line
import sys
x = 'foo'
sys.stdout.write(x + '\n')
# is equal to
import sys; x= 'foo'; sys.stdout.write(x + '\n')

#varaibles declaration
counter = 100    # An integer assignment
miles = 1000.0   # a floating point
name = "John"    # a string

print (counter), print (miles), print (name)

#multiple assignment
a=b=c=1;
name,address,gender = "Nadim","Kathmandu","Male"

#data types
    #numbers
    #string
    #list
    #tuple
    #dictionary
#Numbers
    #int (signed integers)
    #long (long integers, they can also be represented in octal and hexadecimal)
    #loat (floating point )
    #complex


#strings
str ='Hello world!'

print(str)           # Prints complete string
print(str[0])        # Prints first character of the string
print(str[2:5])      # Prints characters starting from 3rd to 5th
print(str[2:]  )     # Prints string starting from 3rd character
print(str * 2   )    # Prints string two times
print(str + "test")   #prints concatenated string

#python lists
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist)  #Prints concatenated lists


# printing all list items by using for loop
for x in range(len(list)):
    print (list[x])
#printing the list using * operator seperated space
print (*list)

#printing the list using * and separate by the comma
print (*list,sep=",")

#printing the list in new line
print (*list,sep="\n")


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print (tuple)            # Prints complete tuple
print (tuple[0])         # Prints first element of the tuple
print (tuple[1])
print (tuple[1:3])       # Prints elements starting from 2nd till 3rd
print (tuple[2:])        # Prints elements starting from 3rd element
print (tinytuple * 2)    # Prints list two times
print (tuple + tinytuple)  #Prints concatenated tuple

print("length of the tuple is:")
print(len(tuple))
#printing all tuple items
for x in range(len(tuple)):
    print(tuple[x])
#tuple is read only or fixed value
#list can change value

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name':'john','code':6734, 'dept':'sales'}

print (dict['one'])   #Prints value for 'one' key
print (dict[2]     )  # Prints value for 2 key
print (tinydict     ) # Prints complete dictionary
print (tinydict.keys())  #Prints all the keys
print (tinydict.values()) #Prints all the values


#iterate over key/value pair in dict and then print
for key, value in tinydict.items():
    print(key,":",value)


#convert from int to float:
x= float(1)
#convert from float to int:
y=int(2.8)
#convert from int to complex:
z = complex(x)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#BASIC  Arithmetic Operations
num1 = 100
num2 = 100
sum = num1 + num2
print(sum)
print("The sum of %d and %d is %d" % (num1, num2, sum))
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))

#userinput
firstNum = input("Enter the first Number:")
secondNum = input("Enter the second Number:")

#add two number
sumTwo = float(firstNum) + float(secondNum)

print("The sum of {0} and {1} is {2}".format(firstNum, secondNum, sumTwo))


num = int(input("Enter any number to test wheather odd or even:"))
if(num%2)==0:
 print("{0} is even".format(num))
else:
 print("{0} is odd".format(num))




