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


