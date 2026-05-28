def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Find the middle element
        mid = (low + high) // 2
        
        # Check if the middle element is our target
        if arr[mid] == target:
            return mid  # Target found! Return its index.
            
        # If target is smaller, ignore the right half
        elif arr[mid] > target:
            high = mid - 1
            
        # If target is larger, ignore the left half
        else:
            low = mid + 1

    return -1  # Target is not in the list