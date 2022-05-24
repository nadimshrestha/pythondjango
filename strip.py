#Syntax of the strip() method
#string.strip([characters])

text = "    madam   "
print(text.strip())   #remove white spaces from left and right

str1 ="madam"
print(str1.strip(" m"))

text ="madam"
print(text.strip("ma"))

#The syntax for PythonString Count()
#Python count function syntax:
#string.count(char or substring, start, end)

#count
url ="https://www.yahoo.com"
url1 ="https://www.facebook.com"
url2 ="https://www.nepaltrekking.com"
print(url.count("w"))
print(url.count("w",9,10))

para ="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
print("Found", para.count("Lorem")," Lorem")

#Syntax of format() function in Python
#templatestring.format(val1,val2...)

print("Welcome to {} s".format("Laba"))
print("Welcome to Guru{} .".format("99"))
print("Welcome to {name} {num}.".format(name="Guru", num="99"))
print("Welcome to {0}{1}.".format("Guru","99"))
print("{} is {} new kind of {} experience!".format("Guru99", "totally", "learning"))

print("the binary to decimal value is :{:d}".format(0b0011))
print("the binary value is: {:b}".format(500))
print("the value is : {:.2f}".format(23.324223))
print("the value is : {:.0%}".format(0.80))
print("the value is : {:_}".format(100000))
print("the value is : {:,}".format(100000))
print("the value is : {:50}".format(40))
print("the value is : {:-}".format(-40))
print("the value is : {:+}".format(40))
print("the value is : {:=}".format(-40))

print("I have {:5} dogs and {:5} cat.".format(2,1))

str1 = "Welcome to Laba Training Center"
print("The length of the string is:", len(str1))
center = " Laba"
print("we are learning at %s ." %(center))
