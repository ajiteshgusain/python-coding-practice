#stack without using oop
list1=[12]

def list_pop(list1):
    if   is_empty(list1):
        return f"list is empty underflow"
    
       

    popped_element=list1.pop()
    
    return f"popped element :{popped_element}"


def is_empty(list1):
    
    #normal 
    # #=========================
    # this python statement works like this agar list ki len =0 hai means true
    # if len(list1)==0:
    #     return True
    
    # False
    ##========================================================
    # a more simplified version 
    #return len(list1)==0 #it will return true if list empty and false if not

    # a more professional version
    #will be as we know a empty list is considered as  false then we use
    #return not list1
    

print(list_pop(list1))
print(list_pop(list1))



