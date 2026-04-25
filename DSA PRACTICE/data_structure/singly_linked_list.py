class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return f"Added {data} at the beginning."

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return f"List was empty, {data} is now the head."
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
        return f"Added {data} at the end."

    def display(self):
        if self.head is None:
            return "The list is currently empty!"
        
        current = self.head
        output = ""
        while current:
            output += f"{current.data} -> "
            current = current.next
        return output + "None"

# --- THE MAIN LAUNCHER ---
if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("\n--- LINKED LIST MENU ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Display List")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                val = input("Enter value to add at start: ")
                print(ll.insert_at_beginning(val))
            
            elif choice == 2:
                val = input("Enter value to add at end: ")
                print(ll.insert_at_end(val))
            
            elif choice == 3:
                print("\nCurrent List Structure:")
                print(ll.display())
            
            elif choice == 4:
                print("Exiting... goodbye!")
                break
            else:
                print("Invalid choice! Please pick 1-4.")

        except ValueError:
            print("Error: Please enter a number, not text.")
        finally:
            print("-" * 25)