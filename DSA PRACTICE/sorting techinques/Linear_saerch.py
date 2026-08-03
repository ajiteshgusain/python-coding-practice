#linear search

def linear_search(arr,key):
    for i in  range(0,len(arr)):
        if key==i:
            return i



arr=[1,2,3,4]
key=int(input("enter key:"))
print(linear_search(arr,key))

