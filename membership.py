
#phython Membership - in , not in
x = 4
y = 8
list = [1,2,3,4,5];
if ( x in list):
 print("Line 1 - x is available in the given list")
else:
 print("Line 1 - x is not available in the given list")
if (y not in list):
 print("Line 2 - y is not available in the given list")
else:
 print("Line 2 - y is available in the given list")

#identity operators - is, is not
x = 20
y = 20
if ( x is y):
    print("x & y Same Identity")
y=30
if (x is not y):
    print("x & y have Different identity")

#Badmas rule for operators

v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;
print("Value of (v+w) * x/y is ", z)

#Array  in python
#arrayName = array.array(type code for data type, [array,items])

import array
balance = array.array('i',[300,200,100,45,452,154,154,68,46,654])
print(balance[1])  #print 2nd index
print(balance)  #print all index
for i in balance:
    print(i,end = " ")
print("Array last element is:", balance[-1]) #print last index

print(balance[1:5])  #slicing operation
balance.insert(2, 500 )   #insert array elements
print(balance)

balance[0]=1      #modify array elements
print(balance)

#array concatination
first = array.array('b',[4, 6, 8])
second = array.array('b',[3, 54, 34])
numbers = array.array('b')
numbers = first + second
print(numbers)
for i in numbers:   #print concatinate numbers
    print(i)

#removing items from an array
first.pop(2)
print(first)
#del also used to delete the itemss
del first[1]
print(first)

#remove array items by value
numbers.remove(4)
print("The length of the array is",len(numbers))



