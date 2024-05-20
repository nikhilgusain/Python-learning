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


# function
def sums(a,b,c):
    sumsa = a+b+c
    #print(sumsa)
    return sumsa
sumss = sums(1,2,3)
print(sumss)


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
