try:
    a = int(input("Enter a num: "))
    print(a)

except Exception as e:
    print(e)
    print("Kya likh ra hai")

finally:
    print("I am inside finally")

# else:
#     print("I am inside else")