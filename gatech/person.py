class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.eyecolor = ("blue",)
        self.age = 2


myperson = Person("David", "Joyner")

print(myperson.firstname)
print(myperson.lastname)
