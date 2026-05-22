


# class Queue:
  
# # 1. The Setup (Constructor)
#     def __init__(self, limit):
#         self.container = []   # This is our internal list
#         self.limit = limit     # The maximum size allowed



#     def is_empty(self):
#         return not self.container
    

    
#     def is_full(self):
#         if len(self.container)==self.limit:
#             return True
    
#         return False
    

#     def Dequeue(self):
#         if   self.is_empty():
#             return f"queue is empty underflow"
#         return f"popped element :{self.container.pop(0)},you new queue: {self.container}"
    

#     def Enqueue(self,element):
#         self.container.append(element)
#         return f"new queue after appending the elements :{self.container}"


#     # def peek(self):
#     #     if self.is_empty():
#     #         return f"sorry but list is empty!!! "
#     #     return f"peeked element:{self.container[-1]}"




#     def display(self):
#         if self.is_empty():
#             return f"queue is empty!!"
        
#         return f"your queue :{self.container}."
    
#     def __str__(self):
#         return f"queue: {self.container}"

# # 2. THE IGNITION SWITCH (Always at the bottom)
# if __name__ == "__main__":
#     # This code only runs if you run THIS file directly.
#     # It won't run if you "import" this file elsewhere.
#     limit=int(input("enter the length of the queue:"))

#     my_queue=Queue(limit)

# # 2. Interaction Phase
#     while True:
#         print("\n--- MENU ---")
#         print("1. Enqueue | 2. Dequeue | 3. Display queue | 4. Exit")
        
#         try:
#             choice = int(input("Enter choice: "))

#             if choice == 1:
#                 if my_queue.is_full():
#                     print(f" queue is full overflow!!")
                    
#                 else:
#                     val = input("Enter value to push: ")
#                     print(my_queue.Enqueue(val))
            
#             elif choice == 2:
#                 print(my_queue.Dequeue())
            
#             elif choice == 3:
#                 # This uses the __str__ method we wrote above!
#                 print(my_queue.display()) 
            
#             elif choice == 4:
#                 print("Exiting... goodbye!")
#                 break
#             else:
#                 print("Invalid choice!")

#         except Exception as e:
#             print(f"{e}")
#         finally:
#             print("Action processed.")
# this is orignal code 


# now  a better code with  nice error handling

# class Queue:
    
#     # 1. The Setup (Constructor)
#     def __init__(self, limit):
#         self.container = []   # This is our internal list
#         self.limit = limit     # The maximum size allowed

#     def is_empty(self):
#         return not self.container
    
#     def is_full(self):
#         if len(self.container) == self.limit:
#             return True
#         return False
    
#     def Dequeue(self):
#         if self.is_empty():
#             return "queue is empty underflow"
#         # Queues are FIFO (First In, First Out). pop(0) removes the first item.
#         return f"popped element :{self.container.pop(0)}, your new queue: {self.container}"
    
#     def Enqueue(self, element):
#         self.container.append(element)
#         return f"new queue after appending the elements :{self.container}"

#     def display(self):
#         if self.is_empty():
#             return "queue is empty!!"
#         return f"your queue :{self.container}."
    
#     def __str__(self):
#         return f"queue: {self.container}"


# # 2. THE IGNITION SWITCH (Always at the bottom)
# if __name__ == "__main__":
    
#     # Secure the limit input so bad typing won't crash the startup
#     while True:
#         try:
#             limit = int(input("enter the length of the queue: "))
#             if limit <= 0:
#                 print("Please enter a positive number greater than 0.")
#                 continue
#             my_queue = Queue(limit)
#             break # Successfully created the queue, break out of initialization loop
#         except ValueError:
#             print("Invalid input! Please enter a valid integer for the queue length.\n")

#     # 3. Interaction Phase
#     while True:
#         print("\n--- MENU ---")
#         print("1. Enqueue | 2. Dequeue | 3. Display queue | 4. Exit")
        
#         try:
#             choice = int(input("Enter choice: "))

#             if choice == 1:
#                 # Option A: Check before asking for input
#                 if my_queue.is_full():
#                     print(" queue is full overflow!!")
#                 else:
#                     val = input("Enter value to push: ")
#                     print(my_queue.Enqueue(val))
            
#             elif choice == 2:
#                 print(my_queue.Dequeue())
            
#             elif choice == 3:
#                 print(my_queue.display()) 
            
#             elif choice == 4:
#                 print("Exiting... goodbye!")
#                 break
#             else:
#                 print("Invalid choice!")

#         except ValueError:
#             print("Please enter a valid number for the choice.")
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")
#         finally:
#             print("Action processed.")



#queue using  pointer concept (not using inbuilt python functions like pop(),push()) doing
#it like it is done in c++  assuming list as static array.
 

