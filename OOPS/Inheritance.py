# access methods and attributes of the superclass

# parent class
class Dog():
    _legs = 4 # class attribute
    def __init__(self,name): # constructor
        self.name = name
    def speak(self, sound): # method
        print(sound)
    def getLegs(self):
        return self._legs

# child class
class Pitbull(Dog):
    def speak(self): # this will overwrite the speak function of parent  class
        print(f"{self.name} barks pit pit")


class Pug(Dog):
    def speak(self):
        print(f"{self.name} barks pug pug")

#Dog object with name dog1
dog1 = Dog("doggy1")
print(dog1.getLegs())
dog1.speak("doggy1 doggy1")
 
# Create a Pitbull object with the name "pit1" and make it speak
Pitbull("pit1").speak()
Pitbull("pit1").speak()

class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def display_info(self):
        print(f"Name: {self.name}, Color: {self.color}")

class Car(Vehicle):
    def __init__ (self, name, color, brand):
        self.name = name
        self.color = color
        self.brand = brand
        self.brand = brand
    def display_info(self): # uses superclass method display_info to print name and color
        super().display_info()
        print("brand : ",self.brand)
    
car1 = Car("car1","red","Toyota")
car1.display_info()
