#insertion sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        # 1. Assume the first unsorted element is 
        # the smallest
    
        # 2. Scavenge through the rest of the list to find the REAL smallest
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index
                #updating the index of the smallest element

            arr[i],arr[min_index]=arr[min_index],arr[i]
# swapping the smallest we found with the first 
# unsorted position 
        return arr

