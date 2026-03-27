def selection_sort(arr):
    #boundary of the code
    n=len(arr)
    #This loop marks the boundary between the sorted part and the unsorted part.

    # i represents the "current hole" we are trying to fill with
    # the smallest possible number.

    # We stop at n - 1 because when only one element is left at 
    # the end, it’s already the largest and doesn't need to be sorted.
    for i in range(0,n-1):
        # assuming the very first element the min value
        minimum=arr[i]
        #taking care of the index of the mim=n value
        position=i

        # This is the Scavenger Hunt. We start looking at the next element (i + 1)
        # and check everything until the very end of the list (n).

        for j in range(i+1,n):
            if minimum>arr[j]:
                minimum=arr[j]
                position=j

            # This is the beauty part. This line is outside the j loop.

            # Once the hunt is over, we take the absolute smallest number we found
            # (arr[position]) and swap it with the number currently sitting in our "hole" (arr[i]).

            # Key Insight: Even if we looked at 1,000 numbers, we only perform one swap 
            # at the very end of the pass.
        arr[i],arr[position]=arr[position],arr[i]


    return arr



        

arr=[64,25,12,22,11]

print(selection_sort(arr))