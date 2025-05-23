"""
Notes:

list[start:stop:step]
[4:0:-1] # reverse  from 4th index to 2nd last excluding index 0
'item' in list          # True or False
list.index(item)      # Returns index
list.count(item)      # How many times it appears
list.pop(index) deletes and returns
del list[index] deletes and do not remove
emptyList1 = []
emptyList2 = list()

for i, ls in enumerate(list3):
    print(i, ls)

l2 = l1.copy() 
this creates a shallow copy, the nested list are shared
okay to use when non nested list 
do not use for nested list as the inner lists are refrenced to same object
in such case use deepcopy form copy module
l3 = copy.deepcopy(l1) # 2 separate list

functions -- len(), min, max, sum, 
sorted(ls), reversed(ls) -- returns a new list

Tuples
tuples are like list but immutable
they are ordered
packing, unpacking, extended unpacking
methods - index, count
sets do no allow duplicates
insertion, deletion and traversal is O(1) on average

Set:
unordered can not use index like st[0]
automatically removes duplicate
can use set theory operations like 
union  |
intersection  &
only in A  -
subset <=
superset >=
equality ==
inequality !=
symmectric diffrence  ^
st = {}
st = set([])
st = set("")
functions = add(x), upadate(iterable), clear(), copy()
remove(x) - error if not found
discard(x) - no error if not found
pop() - removes random element



frozenset 
fs = frzenset([1,2,3])
immutable and hashable


Dictionary:

d = dict(zip(A, B))
d.setdefault("b", 2)   # Adds 'b' if not present

print(dic.get("item", "default"))
| Method                    | Description                          |
| ------------------------- | ------------------------------------ |
| `dict.keys()`             | Returns a view of all keys           |
| `dict.values()`           | Returns a view of all values         |
| `dict.items()`            | Returns a view of key-value pairs    |
| `dict.get(key, default)`  | Returns value for key or default     |
| `dict.pop(key)`           | Removes key and returns its value    |
| `dict.popitem()`          | Removes & returns last inserted item |
| `dict.update(other_dict)` | Merges another dictionary            |
| `dict.clear()`            | Removes all items                    |
| `dict.copy()`             | Returns a shallow copy               |

d.setdefault("b", 2)   # Adds 'b' if not present
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
# {'a': 0, 'b': 0, 'c': 0}


"""
