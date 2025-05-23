#usefunction lsits(), sets(), 
#tuples(), dictionaries() to execute
def lists():
    list1 = [1,2,3,4, "Nikhil", False, .02]
    print(list1)
    #converts to boolean equivalent to bool(lists)
    if list1:#return false if list1 is empty
        print("not empty")
    
    #list of lists
    list2=[[1,2,3,4],['a','b','c']]
    print(list2)
    print(list2[0])         #print list at index 0
    print(len(list2))       #=number of list inside list 2
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
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    list1=[1,2,3]
    list2=2*list1     # This will create [1, 2, 3, 1, 2, 3]
    print(list2)

    
    #list comprehension 
    
    list2=[2*item for item in list1]
    print(list2)

    list1 = list(range(1,10))
    print(list1)
    
    flist =[item for item in list1 if item%2 == 0]
    print(flist)

    st = "My name is Nikhil. I am from Uttarakhad"
    print(st.split())  # .split returns a list
    
    cc = [std.upper() for std in st.split()];
    print(cc)
    
    #filtering with list comprehension
    cc = [std for std in st.split() if len(std)<3]
    print(cc)
    cc = [std for std in range(10) if std%2 == 0]
    print("Even numbers = \nstd")
    print("To uppercase")
    cc=[std.upper() for std in st.split()]
    print(cc)
    
    #basic syntax for nested list comprehension
    #a[expression for outer_item in outer_iterable for inner_item in inner_iterable]
    ll=[[1,2],[3,4],[5,6]]
    print("breaking a list")
    cc=[item for jj in ll for item in jj]
    print(cc)

    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print("transpose is \n",transpose)

    cc = [cp for item in matrix for cp in item if cp%2==0]
    print(cc)


def deictionaries():
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
    print("==========================")
    for i,j in animal:
        print(j)

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

    #usign list to create dic

    anList = [('a',"AA"),('b',"BB"),("c","CC")]
    anDic = {item[0]:item[1] for item in anList}
    
    print(anDic)
    # or 
    anDic = {key:value for key, value in anList}
    print(anDic)
    anList = [('a',"AA","Aaa","asd"),('b',"BB","bb"),("c","CC")]
    anDic = {item[0]:item[1:] for item in anList}
    print(anDic)
    #dic to list
    # Convert dictionary keys to a list
    print(list(anDic.keys()))  # ['a', 'b', 'c']

    # Convert dictionary values to a list
    print(list(anDic.values()))  # [["AA","Aaa], ["BB","bb"], ["CC"]]

    # Convert dictionary items (key-value pairs) to a list of tuples
    print(list(anDic.items()))  # [('a', [1, 2]), ('b', [3, 4]), ('c', [5, 6])]
    deictionaries()
