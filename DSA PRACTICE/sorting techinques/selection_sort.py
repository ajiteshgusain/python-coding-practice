# def selection_sort(arr):
#     n=len(arr)
   

#     for i in range(0,n-1):
#         min_element=arr[i]
#         position=i
#         for j in range(i+1,n):
#             if min_element>arr[i]:
#                 min_element=arr[i]

#                 position=j
#         arr[i],arr[position]=arr[position],arr[i]



#     return arr

# arr=[64,25,12,22,11]

# print(selection_sort(arr))

# *Selection Sort:*
def selection_sort(arr):
    n = len(arr)

    # Step 1: For i = 0 to n-2 (Python uses 0-based index)
    for i in range(0, n - 1):

        # Step 2: Set current element as the initial minimum
        minimum = arr[i]

        # Step 3: Set position = i
        position = i

        # Step 4: For j = i+1 to n-1 (Look through the unsorted part)
        for j in range(i + 1, n):
            # If we find a smaller element, update minimum and position
            if minimum > arr[j]:
                minimum = arr[j]
                position = j

        # Step 5: Swap arr[i] with the smallest element found (arr[position])
        # This places the smallest found element in its correct sorted spot
        arr[i], arr[position] = arr[position], arr[i]

    # Step 6: END
    return arr

# --- Practical Example ---
# You can use the numbers from your quick sort example too!
arr=[64,25,12,22,11]

print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array (Selection Sort):", sorted_arr)