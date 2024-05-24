# class name begin with capital letter by convnetion
# function begin by def
# init stands for initialization
# self is a reference to the current instance of the class. 
    # It is used within class methods to access 
    # instance attributes and other methods of the class.
    # When you create an instance of a class, 
    # self allows each method to refer to and modify a
    # attributes of that particular instance.
    # it is used a function calls another funtion in same class
    # coventional variable name to refer to the class instance.
# print(locals()) - prints local variables
# functions are just variables with data
# print(globasls()) - print global variables
#
# you can have list of function name and use for loop to execute all/some of them
# lamda functions
# Higher-Order Function: takes another function as an argument
# or returns a function or both.

# Attribute - variables within class
# Class attributes - same for all unless overwritten, scope static
#                     by convention begins with _
# Instance attributes - unique to each instance
#                       generally with in __init__ funtion

class Car:
    _wheels = 4 # class attribute

    def __init__(self,brand,year,cost,travel): # constructor called automatticaly
        self.brand = brand # instance attributes
        self.year = year
        self.cost = cost
        self.travel = travel
    def description(self): # methods
        print(f"brand is {self.brand}\nwheels = {self._wheels}\nyear - {self.year}\ncost is {self.cost}\ntravel in km = {self.travel}")

car1=Car("Kwid",2005,23000,516)
car2=Car("Nixan",2016,35000,798)
print("\nWheels = ",Car._wheels)
print("\n     Car 1:")
car1.description()
print("\n     Car 2:")
car2.description()



# Named Parameters

def operations(x, y, operations = "sum"):
    # defaul value of operation = sum will be used if no input provided
    if operations == "sum":
        print('sum = ',x + y)
    if operations == 'mul':
        print("mul = ", x*y)
    if operations == 'div':
        print("Division =  ",x/y)
        
#
operations(10,5,)
operations(2,3, operations = 'mul')
operations(12,4,"div")
