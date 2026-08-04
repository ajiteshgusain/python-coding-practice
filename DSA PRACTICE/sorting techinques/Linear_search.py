#linear search

def linear_search(arr,key):
    comparison=0
    for i in  arr:
        if key==i:
            comparison+1
            return f"element {i} . {comparison} "

    else:
        return  f"key not found . {comparison} "
        



arr=list(range(1,1001))
key=int(input("enter key:"))
print(linear_search(arr,key))



