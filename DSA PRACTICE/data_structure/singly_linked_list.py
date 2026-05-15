# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#         return f"Added {data} at the beginning."

#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return f"List was empty, {data} is now the head."
        
#         last = self.head
#         while last.next:
#             last = last.next
        
#         last.next = new_node
#         return f"Added {data} at the end."

#     def display(self):
#         if self.head is None:
#             return "The list is currently empty!"
        
#         current = self.head
#         output = ""
#         while current:
#             output += f"{current.data} -> "
#             current = current.next
#         return output + "None"

# # --- THE MAIN LAUNCHER ---
# if __name__ == "__main__":
#     ll = LinkedList()

#     while True:
#         print("\n--- LINKED LIST MENU ---")
#         print("1. Insert at Beginning")
#         print("2. Insert at End")
#         print("3. Display List")
#         print("4. Exit")

#         try:
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 val = input("Enter value to add at start: ")
#                 print(ll.insert_at_beginning(val))
            
#             elif choice == 2:
#                 val = input("Enter value to add at end: ")
#                 print(ll.insert_at_end(val))
            
#             elif choice == 3:
#                 print("\nCurrent List Structure:")
#                 print(ll.display())
            
#             elif choice == 4:
#                 print("Exiting... goodbye!")
#                 break
#             else:
#                 print("Invalid choice! Please pick 1-4.")

#         except ValueError:
#             print("Error: Please enter a number, not text.")
#         finally:
#             print("-" * 25)

class Node:
    def __init__(self, data):
        # This stores the actual value (like 10, 20, or "Apple")
        self.data=data
        self.next=None
        #This stores the "address" of the next node. 
 
#  a linked list is a continuous array means
# the nodes formed are assigned address randomly

                          # It starts as None (empty) because there's no next node yet.

# in likd
# creating nodes
node1=Node(10) #node appearence->[10|None]address let 1000
node2=Node(20) #node appearence->[20|None] adrress 20000
# connecting the nodes

node1.next=node2


        
# class Linkedlist:
#     def __init__(self):
#         #When we first create a list, it's empty, so head is None.
#         self.head=None

#     #insertion at the beginning
#     def insert_at_beginning(self, new_data):
#         #create a new node with the data
#         new_node=Node(new_data)
#         # 2. Make the 'next' of this new node point to the current head

#         new_node.next = self.head
#         # 3. Move the head to point to this new node
#         self.head=new_node


#     #deletion 

#     def delete_node(self,key):
#         # start at the begining
#         temp=self.head
#         # CASE 1: If the head itself needs to be deleted
#         if temp is not None:
#             if temp.data==key:
#                 self.head= temp.next# Just move the head to the second node
#                 temp=None #delete the old head from memory
#                 return
            

#         #case 2: search for the key while track of the "previous" node

#         prev=None
#         while temp is not None:
#             if temp.data==key:
#                 break

#             prev=temptemp








        