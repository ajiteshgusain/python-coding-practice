# #stack without using oop
# list1=[]

# def list_pop(list1):
#     if   is_empty(list1):
#         return f"list is empty underflow"
    
       

#     popped_element=list1.pop()
    
#     return f"popped element :{popped_element},you new list: {list1}"



# def is_empty(list1):
    
#     #normal 
#     # #=========================
#     # this python statement works like this agar list ki len =0 hai means true
#     # if len(list1)==0:
#     #     return True
    
#     # False
#     ##========================================================
#     # a more simplified version 
#     return len(list1)==0 #it will return true if list empty and false if not

#     # a more professional version
#     #will be as we know a empty list is considered as  false then we use
#     #return not list1
# def push_list(list1):
#     if is_full(list1):
#         return f" list is full overflow!!"
    
#     element=input("enter the elements for the list:")
#     list1.append(element)

#     return f"new list after appending the elements :{list1}"


# def peek(list1):
#     if is_empty(list1):
#         return f"sorry but list is empty!!! "
#     return f"peeked element:{list1[-1]}"



# def is_full(list1):
#     if len(list1)==length:
#         return True
    
#     return False

# def seek(list1):
#     if is_empty(list1):
#         return f"list is empty!!"
    
#     return f"your list :{list1}"



# length=int(input("enter the length of the list:"))
# while True:
#     print("1. to pop ")
#     print("2. to push")
#     print("3. to seek")
#     print("4. to peek")
#     print("5. to exit")
    

#     choice=int(input("enter your choice:"))

#     try:
        
#         if choice==1:
#             print(list_pop(list1))
            
            
#         elif choice==2:

#             print(push_list(list1))

#         elif choice==3:
#             print(seek(list1))

#         elif choice==4:
#             print(peek(list1))

#         elif choice==5:
#             break

#     except Exception as e:
#         print(print("some error occured"))

#     finally:
#         print("thank you")

    

#=========================================================================
#stack using class

class stack:
  
# 1. The Setup (Constructor)
    def __init__(self, limit):
        self.container = []   # This is our internal list
        self.limit = limit     # The maximum size allowed



    def is_empty(self):
        return not self.container
    

    
    def is_full(self):
        if len(self.container)==self.limit:
            return True
    
        return False
    

    def list_pop(self):
        if   self.is_empty():
            return f"list is empty underflow"
        return f"popped element :{self.container.pop()},you new list: {self.container}"
    

    def push_list(self,element):
        
        if self.is_full():
            return f" list is full overflow!!"
        
        self.container.append(element)


        return f"new list after appending the elements :{self.container}"


    def peek(self):
        if self.is_empty():
            return f"sorry but list is empty!!! "
        return f"peeked element:{self.container[-1]}"




    def seek(self):
        if self.is_empty():
            return f"list is empty!!"
        
        return f"your list :{self.container}."
    
    def __str__(self):
        return f"Stack: {self.container}"

# 2. THE IGNITION SWITCH (Always at the bottom)
if __name__ == "__main__":
    # This code only runs if you run THIS file directly.
    # It won't run if you "import" this file elsewhere.
    limit=int(input("enter the length of the list:"))

    my_stack=stack(limit)

# 2. Interaction Phase
    while True:
        print("\n--- MENU ---")
        print("1. Push | 2. Pop | 3. Display Stack | 4. Exit")
        
        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                val = input("Enter value to push: ")
                print(my_stack.push(val))
            
            elif choice == 2:
                print(my_stack.pop())
            
            elif choice == 3:
                # This uses the __str__ method we wrote above!
                print(my_stack) 
            
            elif choice == 4:
                print("Exiting... goodbye!")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number.")
        finally:
            print("Action processed.")