


class Queue:
  
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
    

    def Dequeue(self):
        if   self.is_empty():
            return f"queue is empty underflow"
        return f"popped element :{self.container.pop(0)},you new queue: {self.container}"
    

    def Enqueue(self,element):
        
        if self.is_full():
            return f" queue is full overflow!!"
        
        self.container.append(element)


        return f"new queue after appending the elements :{self.container}"


    # def peek(self):
    #     if self.is_empty():
    #         return f"sorry but list is empty!!! "
    #     return f"peeked element:{self.container[-1]}"




    def display(self):
        if self.is_empty():
            return f"queue is empty!!"
        
        return f"your queue :{self.container}."
    
    def __str__(self):
        return f"queue: {self.container}"

# 2. THE IGNITION SWITCH (Always at the bottom)
if __name__ == "__main__":
    # This code only runs if you run THIS file directly.
    # It won't run if you "import" this file elsewhere.
    limit=int(input("enter the length of the queue:"))

    my_queue=Queue(limit)

# 2. Interaction Phase
    while True:
        print("\n--- MENU ---")
        print("1. Enqueue | 2. Dequeue | 3. Display queue | 4. Exit")
        
        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                val = input("Enter value to push: ")
                print(my_queue.Enqueue(val))
            
            elif choice == 2:
                print(my_queue.Dequeue())
            
            elif choice == 3:
                # This uses the __str__ method we wrote above!
                print(my_queue.display()) 
            
            elif choice == 4:
                print("Exiting... goodbye!")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number.")
        finally:
            print("Action processed.")