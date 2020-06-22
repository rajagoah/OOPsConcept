"""
Instance attributes --> all classes create object and all objects contain characteristics called attributes.
use __init__() to initialise the first attributes of the object.
You will never have to call the __init__() method. It will automatically get initialized when a new instance of Dog class is created

Class attributes --> While instance attributes are specific to the instance, class level attributes are common to all instances of the class"""

class Dog:

    #class attributes
    species = 'mammals'

    #initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} and {}".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

if __name__ == "__main__":
    a = Dog('Raje', '21')
    print(type(a))
    print(a.description())
    print(a.speak('gruf gruf'))