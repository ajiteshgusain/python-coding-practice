from typing import List, Any, Callable, Optional

class ComprehensiveHeap:
    def __init__(self, mode: str = "min", key: Optional[Callable[[Any], Any]] = None):
        """
        Initializes a flexible Heap.
        :param mode: 'min' for Min-Heap, 'max' for Max-Heap.
        :param key: A function to extract a comparison key from elements.
        """
        if mode not in ("min", "max"):
            raise ValueError("Mode must be either 'min' or 'max'")
        
        self.heap: List[Any] = []
        self.mode: str = mode
        # If no key is provided, use the element identity function
        self.key: Callable[[Any], Any] = key if key else lambda x: x

    def _compare(self, val1: Any, val2: Any) -> bool:
        """Helper to evaluate the heap invariant based on the selected mode."""
        k1, k2 = self.key(val1), self.key(val2)
        if self.mode == "min":
            return k1 < k2
        return k1 > k2

    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        return 2 * index + 2

    def push(self, element: Any) -> None:
        """Inserts an element and restores the heap property in O(log N)."""
        self.heap.append(element)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> Any:
        """Removes and returns the root element in O(log N)."""
        if not self.heap:
            raise IndexError("Pop from an empty heap")
        
        # Swap root with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        root_item = self.heap.pop()
        
        if self.heap:
            self._sift_down(0)
            
        return root_item

    def peek(self) -> Any:
        """Returns the top element without removing it in O(1)."""
        if not self.heap:
            raise IndexError("Peek from an empty heap")
        return self.heap[0]

    def build_heap(self, array: List[Any]) -> None:
        """Transforms a raw list into a valid heap in O(N) linear time."""
        self.heap = list(array)
        # Sift down starting from the last non-leaf node up to the root
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)

    def update_element(self, old_element: Any, new_element: Any) -> bool:
        """Finds and replaces an element, adjusting its tree location."""
        try:
            idx = self.heap.index(old_element)
            self.heap[idx] = new_element
            # Trigger both to ensure correctness regardless of value direction
            self._sift_up(idx)
            self._sift_down(idx)
            return True
        except ValueError:
            return False  # Element not found

    def _sift_up(self, index: int) -> None:
        """Bubbles an element up to restore balance."""
        while index > 0:
            parent_idx = self._parent(index)
            if self._compare(self.heap[index], self.heap[parent_idx]):
                self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
                index = parent_idx
            else:
                break

    def _sift_down(self, index: int) -> None:
        """Sinks an element down to restore balance."""
        size = len(self.heap)
        while self._left_child(index) < size:
            target_idx = self._left_child(index)
            right_idx = self._right_child(index)

            # Check if right child exists and satisfies the target condition better
            if right_idx < size and self._compare(self.heap[right_idx], self.heap[target_idx]):
                target_idx = right_idx

            # If the current node is already in the right spot, stop
            if self._compare(self.heap[index], self.heap[target_idx]) or self.heap[index] == self.heap[target_idx]:
                break

            self.heap[index], self.heap[target_idx] = self.heap[target_idx], self.heap[index]
            index = target_idx

    def __len__(self) -> int:
        return len(self.heap)

    def __str__(self) -> str:
        return f"{self.mode.capitalize()}-Heap Structure: {self.heap}"
tasks = [
    {"name": "Fix minor bug", "priority": 3},
    {"name": "Database crash", "priority": 1},
    {"name": "Write documentation", "priority": 4},
    {"name": "Deploy security patch", "priority": 2}
]

# Initialize heap with a lambda key targeting the priority value
task_heap = ComprehensiveHeap(mode="min", key=lambda x: x["priority"])
task_heap.build_heap(tasks)

print(task_heap)
print("Processing:", task_heap.pop()) # Will process priority 1 (Database crash)
print("Next up:", task_heap.peek())   # Will show priority 2 (Deploy security patch)
