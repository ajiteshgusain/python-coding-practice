class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Linked_list:# manager of our list
    def __init__(self):
        self.head=None# starting point of list must be empty

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return


#If the list was not empty, we need to find the last box.
#We create a temporary pointer called current and start it at the very first box       
        current =self.head
        while current.next is not None:
            current=current.next
        current.next=new_node


# list trversal
    def print_list(self):
        current= self.head
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print ("None")