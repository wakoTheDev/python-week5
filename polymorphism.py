# Base Class: Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


# Derived Classes: Dog, Bird, and Fish
class Dog(Animal):
    def move(self):
        return "Running on four legs ."


class Bird(Animal):
    def move(self):
        return "Flying in the sky ."


class Fish(Animal):
    def move(self):
        return "Swimming in the water ."


# Using the Classes
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())
