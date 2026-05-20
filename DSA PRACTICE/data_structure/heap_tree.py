class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        # 1. Add element to the end of the array
        self.heap.append(val)
        # 2. "Bubble up" to maintain heap property
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()
        
        # 1. Replace root with the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # 2. "Bubble down" to restore order
        self._bubble_down(0)
        return root

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    def _bubble_down(self, index):
        smallest = index
        left, right = 2 * index + 1, 2 * index + 2
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)




class Node:
    def __init__(self, key):
        self.value = key  
        self.left = None  
        self.right = None    

# Creating the root node
root = Node(5)