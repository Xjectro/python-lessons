class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


class Car:
    alive = False  # Not an animal, but has an alive attribute

    def speak(self):  # Not an animal, but has a speak method
        print("Beep!")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
