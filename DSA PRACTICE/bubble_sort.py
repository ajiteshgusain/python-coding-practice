#bubble sort 
#the basic idea of the bubble sort is to compare two adjoining elements and exchange them if
# they  are in not proper order.
list=[15,6,13,22,3,52,2]



#bubble sort 
#the basic idea of the bubble sort is to compare two adjoining elements and exchange them if
# they  are in not proper order.
list=[15,6,13,22,3,52,2]

def bubble_sort(list):
    n=len(list)
    count=0
    #traverse through all list elements
    for i in range(0,n):
        
        #last i elements  are already in place
        for j in range(0,n-i-1):

        #this expression  will ensure that we  do not compare 
        # the heavier elements that have already settled at correct place.
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]

         

    

    return list


        #print("sorted list using bubble sort:",list)
    #print("no of iterations:",count)





print(bubble_sort(list))





#optimized  bubble sort










def bubble_sort(list):
    n=len(list)
    count=0
    #traverse through all list elements
    for i in range(0,n):
        swapped=False
        #last i elements  are already in place
        for j in range(0,n-i-1):

        #this expression  will ensure that we  do not compare 
        # the heavier elements that have already settled at correct place.
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]

                swapped=True

        if not swapped:
            break
    

    return list


        #print("sorted list using bubble sort:",list)
    #print("no of iterations:",count)





print(bubble_sort(list))