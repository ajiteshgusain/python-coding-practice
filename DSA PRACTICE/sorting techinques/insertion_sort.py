#selection sort: it works like this as it check one element at a time from the unsorted list
# by inserting th element at its correct position in sorted list.
list=[15,6,13,22,3,52,2]
def insertion_sort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j=j-1

            # print(list)
        else:
            list[j+1]=key
            # print(f"insertion{key} in list")
            # print(list)

        break


    return list










print(insertion_sort(list))