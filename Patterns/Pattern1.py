'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''
i = 5
while i >= 1:
    j = 1
    while j<=i:
        print(j, end = " ")
        j+=1
    i-=1
    print()
print("-------------------------------")

'''
1
12
123
1234
12345
'''
i = 1
while i <= 5:
    j = 1 
    while j<=i:
        print(j, end = " ")
        j+=1
    print()
    i+=1


'''
1       1  
12     21     
123   321      
1234 4321       
1234554321
'''
print("================================================")
j = 1

while j<=5:
    i = 1
    while i <=j:
        print(i, end = " ")
        i+=1
    k=1
    while k<=5-j:
        print(" ", end = " ")
        k+=1
    k=1
    while k<=5-j:
        print(" ", end = " ")
        k+=1
    i=j
    while i >=1:
        print(i, end = " ")
        i-=1
    print()
    j+=1