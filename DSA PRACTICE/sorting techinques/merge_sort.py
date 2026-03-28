def merge_sort(arr):
    if len(arr)<=1:
        # it means the list has one single element
        # which means it i sorted 
        return arr
    #dinfing the middle and split the list
    mid=len(arr)//2
    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])

    #now start merging the two sorted halves
    return merge(left_half,right_half)

def  merge(left,right):

    sorted_list=[]
    #i tracks left half list  ,j tracks right half list
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_list.append(left[i])
            i+=1

        else:
            sorted_list.append(right[j])
            j+=1


    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list



arr=[34,65,2,1,1,46]
result=merge_sort(arr)

print(result)
