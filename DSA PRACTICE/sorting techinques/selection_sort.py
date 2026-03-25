#insertion sort
def selection_sort(arr):
    n=len(arr)
    for i in range(1,n-1):
        min=arr[i]
        pos=i
        