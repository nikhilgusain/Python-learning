from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        print("class - Animal's method")

class Dog(Animal):
    def make_sound(self):
        print("Bhau Bhau")
    def __str__(self):
        return "Dog class"

d1 = Dog()
print(d1)
print(d1.make_sound())