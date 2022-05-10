#def function_name(parameter):
#"""docstring"""
#statement(s)


#function definition
def greet(name):
    # """docstring"""
    """
    This function greets to
    the person passed in as
    a parameter
    """
    # functions statement
    print("hello," + name + ". Good Morning")

name = input("Enter you Name?")
greet(name)


#example of return
def absolute_value(num):
    """this function returns the absolute
    value of the entered number"""
    if num >= 0 :
        return num
    else:
        return -num
print(absolute_value(2))
print(absolute_value(-4))

#variable scope
def my_func():
    x=10
    print("Value inside function:",x)
x=20
my_func()
print("value outside function",x)

#Python Default Arguments
#Function arguments can have default values in python.
#we can provide a default value to an argument by using the assignment operator(=).
#here is an example.
def sum1(num1=10, num2=10):
    sum = num1+num2
    return sum
total = sum1(30)
print(f"the total is {total}")

#Python Arbitrary Arguments
def greet (*names):
    """This function greets all
    the person in the names tuple.  """
    #names is a tuple with arguments
    for name in names:
        print("Hello", name)
greet("Monica", "Luke", "Steve", "John")

#nonlocal variable
#This means that the variable can be neither in the local nor the global scape.
def outer():
    x="local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:",x)
    inner()
    print("outer:",x)
outer()

#Changing Global variable from inside a function using global
c= 0 #Global variable
def add():
    global c
    c = c+2 #increment by 2
    print("Inside add():",c)
add()
print("In main:",c)










