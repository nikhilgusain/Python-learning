# variables
x = 10
y = 20
z = 3.33
sum1 = x+y
sum2 = z+x

print("sum1=",sum1)
print("sum2= ",sum2)

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


#Data structures

#list
list1 = [1,2,3,4, "Nikhil", False, .02]
print(list1)
#list of lists
list2=[[1,2,3,4],['a','b','c']]
print(list2)
print(list2[0])
print(len(list2))
print([1,2]==[2,1])
list1.append(77)
print(list1)


#sets
#all elements are unique
#can not use append
set1={1,2,35,4,6,}
print(set1)
set2={1,2,35,4,6,4,6,6,99,1}
print(set2)
print(len(set2))
print({1,2,3} == {1,1,1,3,2,3})

#tuple
#can never be changed once declared
#memory efficient
#good to store x,y corrdinate pairs
tup={1,2,3}
print(tup)

#dictionary
#unique keys
#if multiple former will replace previous
dic1={
    'apple':"red",
    'bear':'animal',
    1:'one'
}
print(dic1)
print(dic1['apple'])
print(dic1[1])


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

