# *Quick sort:* 

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[low]   # first element as pivot
    i = low + 1
    j = high

    while True:
        # move i right until element > pivot
        while i <= j and arr[i] <= pivot:
            i += 1
        
        # move j left until element <= pivot
        while i <= j and arr[j] > pivot:
            j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    # place pivot at correct position
    arr[low], arr[j] = arr[j], arr[low]
    
    return j

arr = [10, 7, 8, 9, 1, 5]

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)