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