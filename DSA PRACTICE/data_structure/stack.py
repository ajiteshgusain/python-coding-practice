#stack without using oop
list1=[]

def list_pop(list1):
    if   is_empty(list1):
        return f"list is empty underflow"
    
       

    popped_element=list1.pop()
    
    return f"popped element :{popped_element},you new list: {list1}"



def is_empty(list1):
    
    #normal 
    # #=========================
    # this python statement works like this agar list ki len =0 hai means true
    # if len(list1)==0:
    #     return True
    
    # False
    ##========================================================
    # a more simplified version 
    return len(list1)==0 #it will return true if list empty and false if not

    # a more professional version
    #will be as we know a empty list is considered as  false then we use
    #return not list1
def push_list(list1):
    if is_full(list1):
        return f" list is full overflow!!"
    
    element=input("enter the elements for the list:")
    list1.append(element)

    return f"new list after appending the elements :{list1}"


def peek(list1):
    if is_empty(list1):
        return f"sorry but list is empty!!! "
    return f"peeked element:{list1[-1]}"



def is_full(list1):
    if len(list1)>length:
        return True
    
    False

def seek(list1):
    if is_empty(list1):
        return f"list is empty!!"
    
    return f"your list :{list1}"



length=int(input("enter the length of the list:"))
while True:
    print("1. to pop ")
    print("2. to push")
    print("3. to seek")
    print("4. to peek")
    

    choice=int(input("enter your choice:"))

    try:
        
        if choice==1:
            list_pop(list1)
            
            
        elif choice==2:

            push_list(list1)

        elif choice==3:
            seek(list1)

        if choice==4:
            peek(list1)

    except Exception as e:
        print("some error occured")

    finally:
        print("thank you")

    break


    



