arr = [10,20,30,40,50,60,70,80,90,100]
l=0
r=len(arr)-1
key = int(input("Enter key: "))
flag = True

while l<=r:
    mid = (l+r) // 2
    if arr[mid] == key:
        print(f"found at {mid}")
        flag = False
        break
    elif arr[mid]>key:
        r=mid-1
    else:
        l=mid+1

if flag:
    print("not found")
