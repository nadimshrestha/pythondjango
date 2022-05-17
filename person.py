class Person:
    # init method or constructor
    newname="";
    def __init__(self, na):
        self.name = na
        print('Hello, my name is', self.name)
    #Sample Method
    def say_hi(self, nickname):
        self.newname=nickname
        print('Hello, my nickname is', self.newname)
    def say_bye(self):
        print("Good Bye")
p = Person('Nikhil')
p.say_hi("Nickname")
p.say_bye()