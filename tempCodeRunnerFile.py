
def operations(x, y, operations = "sum"):
    # defaul value of operation = sum will be used if no input provided
    if operations == "sum":
        print('sum = ',x + y)
    if operations == 'mul':
        print("mul = ", x*y)
    if operations == 'div':
        print("Division =  ",x/y)
    print(f"local variables ar{locals()})

operations(10,5,)
operations(2,3, operations = 'mul')
operations(12,4,"div")
