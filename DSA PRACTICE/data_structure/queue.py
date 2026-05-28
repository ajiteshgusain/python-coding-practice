# ==========================================
# SETUP AND INITIALIZATION
# ==========================================
queue = [0] * 100
n = 100
front = -1
rear = -1

# ==========================================
# FUNCTION TO INSERT AN ELEMENT (ENQUEUE)
# ==========================================
def insert():
    global front, rear
    if rear == n - 1:
        print("\n❌ Queue Overflow! The queue is completely full.")
    else:
        if front == -1:
            front = 0
        val = int(input("Insert the element in queue: "))
        rear += 1
        queue[rear] = val
        print(f"✅ {val} successfully added to the queue.")

# ==========================================
# FUNCTION TO DELETE AN ELEMENT (DEQUEUE)
# ==========================================
def delete():
    global front, rear
    if front == -1 or front > rear:
        print("\n❌ Queue Underflow! There is nothing to delete.")
    else:
        print("\n🗑️ Element deleted from queue is:", queue[front])
        front += 1

# ==========================================
# FUNCTION TO DISPLAY THE QUEUE
# ==========================================
def display():
    if front == -1 or front > rear:
        print("\n📭 Queue is empty")
    else:
        print("\n🔹 Queue elements are:", end=" ")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print() # New line for neatness

# ==========================================
# MAIN MENU LOOP (To interact with the code)
# ==========================================
while True:
    print("\n--- QUEUE OPERATIONS ---")
    print("1. Insert (Enqueue)")
    print("2. Delete (Dequeue)")
    print("3. Display Queue")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a number between 1 and 4.")