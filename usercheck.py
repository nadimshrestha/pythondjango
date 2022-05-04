#username and password checking
username = input("Enter the username:")
password = input("Enter the password:")

if(username == "admin" and password == "P@ssw0rd"):
    print("Credential Match")
else:
    print("Invalid Username or Password")