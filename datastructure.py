#Data structures
#list
list1 = [1,2,3,4, "Nikhil", False, .02]
print(list1)
#converts to boolean equivalent to bool(lists)
if list1:
    print("not empty")
#list of lists
list2=[[1,2,3,4],['a','b','c']]
print(list2)
print(list2[0])
print(len(list2))
print([1,2]==[2,1])
#append(num) - adds at end 
list1.append(77)
print(list1)
#pop() - remove from end
list1.pop()
print(list1)
print(list1[::2])
#does not include 17
list1 = list(range(17))
print(list1)
#listName.insert(index, item)
list1.insert(4,'nimo')
print("-----------------------")
print(list1)
#listName.remove(only one item)
list1.remove(4)

# a and b are same changign one will change other also 
a = [1,2,3,4,5,6,7,8]
b = a

#copies all of a to c

c = a.copy ()
b.pop()
print(a)
print(c)

#sets
#all elements are unique
#can not use append
set1={1,2,35,4,6,}
print(set1)
set2={1,2,35,4,6,4,6,6,99,1}
print(set2)
#length is after removing duplicate
print(len(set2))
#next line is true
print({1,2,3} == {1,1,1,3,2,3})
set2 = {'a','b','j','d'}
set2.add('c')
print(set2)
while set2:
    print(set2.pop())

#tuple
#can never be changed once declared
#memory efficient
#good to store x,y corrdinate pairs
tup={1,2,3}
#can work wothout comma when declarign 
#default type when returning multiple values 
# ex return 1,5,3 is tuple

tup2 = a,b,c
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
print(dic1.keys())
# dicName.get('search key', "return this if not found" )
animal = {
    'b':['bull', 'bat', 'bison'],
    'c':['cat', 'cow'],
    'f':["fish","falcon"]
}

animal['b'].append("black")#adds black if b exists
print(animal)

#if key do not exit will give error
#animal['t'].append("tt") will give error

#if c is in dictionary it will add like normal
animal['c'].append("cebra")

if 'z' not in animal:
    animal['z'] ="zebra"#creates new key in diec

print(animal)
print("___________")
from collections import defaultdict
animal = defaultdict(list)
animal['k'].append("kangaroo")
print(animal)
