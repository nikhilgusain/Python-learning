# variables
x = 10
y = 20
z = 3.33
sum1 = x+y
sum2 = z+x

print("sum1=",sum1)
print("sum2= ",sum2)

#datatypes
print(int(8.9))
print(int(14/3))
print(round(14/3, 2))
print(round(14/3, 5))

print(int('100'))
#has to be string, base 2
print(int('100',2))
print(int('1ab',16))

#loops
print("while loop")
i = 0 
while i <= 5:
    print(i)
    i+=1

print("for loop")
#automatically begins index from 0
for i in range (5):
    print(i)
    

if sum1>22:
    print("greater than 22")
else:
    print('less than 22')

if(sum1==22):
    print("sum1 = 22")
elif(sum1<22):
    print("sum1<22")
else:
    print("sum1>22")


#operators
#string
st = "nik "
st2 = 4 * st
st = st + st
print(st2)

#membership operator
print(1 in[10,20,30,1,2,2,], 10 in [1,2,3,55])
print('cat' in 'this is not a cat')

# function
def sums(a,b,c):
    sumsa = a+b+c
    #print(sumsa)
    return sumsa
sumss = sums(1,2,3)
print(sumss)

print(print('jj'))
#print is a function that return
#list 
name = ["Nikhil", "Varun", "Akhshara", "Patel", "Jashmine", "Mahesh", "Isha", "Nikita", "Sumit"]
age = [1,2,3,4,5,6,7,8,9]
print("using for ")
for i in name:
    print(i)

print("using while and index ")

i = 0
while i < len(age):
    print(name[i])
    i = i+1

print("using zip ")
for nam, ag in zip(name, age):
    print(f"{nam},{ag}")

print("             reversed ")
for m in reversed(name):
    print(m)

# enumerate
for j, nam in enumerate(name):
    print(f"{j}, {nam}")




#               class
# variable inside a class are called variable
# funcitons inside a class are called method
print("--------------class----------------")
#class name should start with capital letter 
class Dogg:
    def __init__(self):#constructor
        self.name = "Doggy"
        self.legs = 4
    def speak(self):
        print(self.name + " barks ")


#myDog = Instance of Dog class
myDog = Dogg()
anotherDog = Dogg()

#calling th speak method

#class instance is also called object
#using the dot funciton acts as if you are 
#passing you instance as your first variabel

#notice the self argument in speak funtion, argument 
#passed is the instance of class  itself i.e. object

myDog.speak()

class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4
    def speak(self):
        print(self.name + " bark ")

myDog = Dog("DOOBY")
myDog.speak()

st = 'My name is Nikhil Gusain'
#does not include index 6
st1 = st[0:6]
print(st1)
#include 6
print(st[6:])

st = 'my number is ' + str(55)
print(st)
st = 'my number is ' + "55"
print(st)
#f stands for formated
st = f'my number is {55}'
print(st)
st = f'my number is {55} and twice of it is {55*2}'
print(st)
import math
print(f'pi = {math.pi:.2f}')

st = '''here is 
a long 
text 
in diff line'''
print(st)
