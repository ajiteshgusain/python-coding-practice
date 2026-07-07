# #selection sort: it works like this as it check one element at a time from the unsorted list
# # by inserting th element at its correct position in sorted list.
# list=[15,6,13,22,3,52,2]
# def insertion_sort(list):
#     for i in range(1,len(list)):
#         key=list[i]
#         j=i-1
#         while j>=0 and key<list[j]:
#             list[j+1]=list[j]
#             j=j-1

#             # print(list
#         else:
#             list[j+1]=key
#             # print(f"insertion{key} in list")











# print(insertion_sort(list))


# revising it .

def insertion_sort(arr):
    # We start from the second element (index 1) 
    # because the first element is already "sorted" by itself.
    for i in range(1,len(arr)):
        key=arr[i]# The "card" we are currently picking up
        j = i - 1     # The index of the item just to the left of our key
        

    # Compare the key with each element to its left 
        # until a smaller element is found or we reach the start.

        while j>=0 and key<arr[i]:
            







