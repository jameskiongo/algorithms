class Name:
    def __init__(self):
        self.firstname = "james"
        self.lastname = "kiongo"


class Person:
    def __init__(self):
        self.name = Name()
        self.eyecolor = "blue"
        self.age = 1


person = Person()

print(person.name)
