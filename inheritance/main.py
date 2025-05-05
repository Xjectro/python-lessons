class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"
    
