import math
#prime number
num = 100
l=[2]
for i in range(3, 100):
    flag = 1
    for j in l:
        if j>math.sqrt(i): #no need to check if j>sqrt(i)
            break
        if i%j == 0:
            flag = 0
            break
    if flag:
        l.append(i)
print(l)