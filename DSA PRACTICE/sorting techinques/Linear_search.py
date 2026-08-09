# #linear search

# def linear_search(arr,key):
#     comparison=0
#     for i in  arr:
          #comparison+1

#         if key==i:
#             
#             return f"element {i} , no of comparsions {comparison} "

#     return  f"key not found .no of comparisons {comparison} "
        



# arr=list(range(1,1001))
# key=int(input("enter key:"))
# print(linear_search(arr,key))



# linear search


def linear_search(arr, key):
    comparison = 0
    for i in arr:
        comparison += 1  # Increment on every check
        if key == i:
            return f"element {i} . comparisons: {comparison}"

    # Placed OUTSIDE the loop so it checks every item before failing
    return f"key not found . comparisons: {comparison}"


arr = list(range(1, 1001))
key = int(input("enter key: "))
print(linear_search(arr, key))