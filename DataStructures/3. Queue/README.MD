# Queues

Imagine standing in line to buy movie tickets. The first person in line gets served first, and anyone joining the queue goes to the end. This real-life scenario perfectly illustrates how a queue works in computer science: it follows the **First In, First Out (FIFO)** principle. In queues, the first item added is the first one removed.

Queues are widely used in scheduling systems, breadth-first search algorithms, and buffering data streams.

## Queues Operations Visualization

Below is a helpful visualization of common Queues operations, complexities, and sorting algorithms, the entire diagram is at [Technical Interview Mindmap](https://coggle.it/diagram/W5E5tqYlrXvFJPsq/t/master-the-interview-click-here-for-course-link):

---

## **Table of Contents**

1. [Introduction to Queues](#introduction-to-queues)  
2. [Deques: Double-Ended Queues](#deques-double-ended-queues)  
3. [Common Operations and Their Complexities](#common-operations-and-their-complexities)  
4. [Queue Implementations in Python](#queue-implementations-in-python)  
5. [Key Points](#key-points)  
6. [Example Code Snippets](#example-code-snippets)  
7. [Solved Problems](#solved-problems)

---

## **Introduction to Queues**

A queue is a linear data structure that allows elements to be added at one end (the rear) and removed from the other end (the front). This behavior is commonly referred to as **First In, First Out (FIFO)**.

### **Supported Operations**:
1. **Enqueue (Push):** Add an element to the rear of the queue.  
2. **Dequeue (Pop):** Remove the front element from the queue.  
3. **Peek:** View the front element without removing it.

---

## **Deques: Double-Ended Queues**

Imagine a bookshelf where you can add or remove books from both ends. This is how a **deque (Double-Ended Queue)** works, providing flexibility by allowing operations at both the front and the rear.

### **Supported Operations**:
1. **Push Front:** Add an item to the front.  
2. **Push Back:** Add an item to the rear.  
3. **Pop Front:** Remove an item from the front.  
4. **Pop Back:** Remove an item from the rear.  
5. **Peek Front:** View the item at the front without removing it.  
6. **Peek Back:** View the item at the rear without removing it.  

Python’s `collections.deque` class provides a highly efficient implementation of both queues and deques.

---

## **Common Operations and Their Complexities**

| Operation         | Time Complexity | Description                                                                 |
|-------------------|-----------------|-----------------------------------------------------------------------------|
| Enqueue (Push)    | **O(1)**        | Add an element to the rear of the queue.                                    |
| Dequeue (Pop)     | **O(1)**        | Remove an element from the front of the queue.                              |
| Peek              | **O(1)**        | View the front element without removing it.                                 |
| Iteration         | **O(n)**        | Loop through all elements in the queue.                                     |
| Search            | **O(n)**        | Find an element; requires linear traversal.                                 |

---

## **Queue Implementations in Python**

### Using `collections.deque`:
Python's `collections.deque` is ideal for implementing queues and deques. It provides efficient O(1) time complexity for append and pop operations from both ends.

### From Scratch (Circular Buffer):
Queues can also be implemented using arrays or linked lists. To improve efficiency, a **circular buffer** can be used to avoid unused space caused by linear array implementations.

---

## **Key Points**
- **FIFO Principle:** The first item added is the first to be removed.  
- **Efficient Operations:** Enqueue and dequeue are O(1) operations with `deque`.  
- **Dynamic Resizing:** Python’s `deque` dynamically handles resizing, unlike a static array.

---

## **Example Code Snippets**

### Queue Implementation Using `deque`:
```python
from collections import deque

# Initialize a queue
queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

# Peek at the front element
print(queue[0])  # Output: 10

# Dequeue an element
print(queue.popleft())  # Output: 10

# Check if the queue is empty
print(len(queue) == 0)  # Output: False
```

### Rotating a Queue Until Zero is at the Front:
```python
from collections import deque
from typing import List

def rotate_left_till_zero(nums: List[int]) -> List[int]:
    queue = deque(nums)
    while queue[0] != 0:
        queue.append(queue.popleft())
    return list(queue)

# Example usage
nums = [1, 2, 3, 0, 4]
print(rotate_left_till_zero(nums))  # Output: [0, 4, 1, 2, 3]
```

### Implementing a Queue from Scratch:
```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("peek from empty queue")
    
    def is_empty(self):
        return len(self.queue) == 0

# Usage
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
print(my_queue.peek())  # Output: 10
print(my_queue.dequeue())  # Output: 10
```

---

## **Solved Problems**

Below are links to solved queue-related problems with explanations:

| Problem Name              | Difficulty | Solution Link                                   |
|---------------------------|------------|-----------------------------------------------|
| Rotate Queue              | Easy       | [Rotate Queue Solution](problems/rotate_queue.py) |
| Circular Buffer           | Medium     | [Circular Buffer Solution](problems/circular_buffer.py) |
| Sliding Window Maximum    | Hard       | [Sliding Window Maximum Solution](problems/sliding_window.py) |

---