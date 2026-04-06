# The Anatomy of a Node
# Before we build the list, we need to build the Node. Think of a Node as a person in a treasure hunt holding a piece of paper:

# Data: The actual treasure (the value).

# Next: The map telling them who the next person in the hunt is.



class Node:
    def __init__(self,data):
        self.data=data#  this is the value we store
        self.next=None#the map to reach  next person (start as empty)

class LinkedList:
    def __init__(self):
        self.head=None#first person in the line
        # if head is none then list is empty
    


    def insert_at_end(self,data):

        #create anew person with data
        new_node=Node(data)

        
        #if list is empty , make this new person the head 
        if self.head is None:
            self.head=new_node

            return
        
        #if not empty then we have to 
        # walk from head till the last node
        last=self.head
        while last.next:#while there is someone  after the current person
            last=last.next#move to the next person

        
        last.next=new_node    
        #now that we are at the last person
        # point their next node to our new node


    def display(self):
        #start from the beginning 
        current=self.head
        #walk through the list untill we hit None (THE end)

        while current:
            print(f"{current.data}",end=" ")
            current=current.next

        print("None")

# --- THE MAIN LAUNCHER ---
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    
    ll.display() # Output: 10 -> 20 -> 30 -> None