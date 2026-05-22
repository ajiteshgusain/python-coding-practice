class Node:
    def __init__(self,data):
        self.data=data
        self.next=None# this is acting like  a connection "->"

#now we are writing the code to add more 
# new nodes at the end of our chsan
class Linked_list:# manager of our list

# when we create a new list it does not have any elements
# initially hence self.head =None acts as starting point from where the 
#new linked lsit will begin
    def __init__(self):
        self.head=None# starting point of list must be empty
#(starting point )|->

#now we are writing the code to add more 
# new nodes at the end of our chain
    def append_at_end(self,data):
        #funct to add new data at the end pf the new list 
        new_node=Node(data)# creating a new node using classs Node

        if self.head is None:#checking if linked list empty
            self.head=new_node
            return
        #then the the starting point (self.head) starts to points this  new node like this |->[new_node] and
        # this new node is our first node of our new   empty list  list 


#If the list was not empty, we need to find the last box.
#We create a temporary pointer (current) and start it at the very first box
# this [current] will pass through every node  from first to last        
# hence ,intial value of current will be self.head means first node
# ""general linked list ""

#|->[self.head]->[next_node]->. . .->->[last_node]->[none]-_ 

        current =self.head
        while current.next is not None:
            current=current.next
            #|->[current]->self.head->[current]->[next_node]->. . .->[last_node]-_[none]
            # we are roaming in the linked list to reach reach the end
        current.next=new_node
        #|->self.head->[next_node]->. . .->[last_node]-[current]->[none]
        #the current will find the end at all cost !!!!
        #as the loop finishes current succeeded in his mission in finding the end the node that points to ->[none] of the list
        # right now we are at last box  which points to none and current is exactly there
        
        #  none to point to new node now new node is connected and this new node will point to none th hence 
        # becoming the gate keeper of list .

        


# list trversal
    def print_list(self):
        current= self.head
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print ("None")



    def search(self,target):
        current=self.head
        # Step 1: Put your finger on the first box
    
    # Step 2: Keep walking as long as your finger is on an actual box
        while current is not None:
            if current.data==target:# Step 3: Check inside the box
                return True # Found it! Stop everything and celebrate.
            
            current= current.next# Step 4: Follow the arrow to the next box

        #we get noting the target element is not in our list
        return False
    

# here we use two pointer technique
#current: The leading finger that checks if this is the box we want to delete.
#prev (Previous): A trailing finger that stays exactly one box behind current.
    def deletion(self,key):
        current=self.head
        prev=None
# Case A: What if the very FIRST box 
# (the Head) is the one to delete?

        if current is not None and current.data==key:
# Move the head pointer to the second box
            self.head=current.next

# Free the old head box from memory
            current=None
            return

# Case B: Walk the chain to find the key 
# So, the phrase "Is current standing on a real box?" means the loop safely verifies: "Hey, is my finger actually pointing to a real,
# valid box right now? If it is pointing to None, I need to s
# top immediately so I don't crash the program."
        while current is not None and current.data !=key:
     # Move 'prev' to where 'current' is standing       
            prev=current

# Slide 'current' forward to the next box
            current = current.next

# Case C: What if the key wasn't even in our list?
        if current is None:
            print ("value  not found i the list !!!")

            return

# Case D: We found it! Unlink the node from the chain
        prev.next=current.next # Bypass 'current' completely!
# Erase the deleted node from memory
        current =None


    def insert_at_position(self,position,data):

        new_node=Node(data)
        if position==0:
            #Make new box point to the old first box
            new_node.next=self.head

            self.head=new_node
            return f"Successfully added {data} at index{position}. "
        current=s
            

#very important 

# 4. Unlinking the Chain
# prev.next = current.next

# Let’s translate that line: "Take the arrow coming out of the box prev is holding (10), and change it to point to whatever is next after current (30)."

# 10 now points directly to 30. The box 20 is isolated!

# current = None wipes our temporary pointer away, completing the bypass operation.







# 🛠️ The Three Scenarios
# When inserting by a position number (index), your code has to handle three possibilities:

# Index 0 (The Front): The list isn't empty, but you want to make this new box the very first item.

# Index in the Middle: You want to insert it somewhere between two existing boxes.

# Index out of bounds: The user asks to insert at index 100, but your list only has 3 boxes!