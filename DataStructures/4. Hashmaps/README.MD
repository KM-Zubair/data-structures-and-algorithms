# Hashmaps

Imagine you need to store and retrieve data efficiently based on keys, such as finding a person's details using their name. A **Hashmap** is a data structure that makes this possible, offering fast access and storage using a **Hash Function**. In Python, it's implemented as a `dictionary`.

Hashmaps are built upon the principle of hashing, where data is mapped to fixed-size values (hashes) for efficient retrieval and storage.

---

## Hashmaps Operations Visualization

Below is a helpful visualization of common Hashmaps operations, complexities, and sorting algorithms, the entire diagram is at [Technical Interview Mindmap](https://coggle.it/diagram/W5E5tqYlrXvFJPsq/t/master-the-interview-click-here-for-course-link):

<img src="images/Hashmaps_1.png" alt="Hashmaps Operations Visualization" width="600">

## **Table of Contents**

1. [Introduction to Hashmaps](#introduction-to-hashmaps)  
2. [Hash Functions](#hash-functions)  
3. [How Hashmaps Work](#how-hashmaps-work)  
4. [Handling Collisions](#handling-collisions)  
   - [Separate Chaining](#separate-chaining)  
   - [Open Addressing](#open-addressing)  
5. [Efficiency](#efficiency)  
6. [Hashmap Implementations in Python](#hashmap-implementations-in-python)  
7. [Key Points](#key-points)  
8. [Example Code Snippets](#example-code-snippets)  
9. [Solved Problems](#solved-problems)

---

## **Introduction to Hashmaps**

A **Hashmap** is a data structure that maps keys to values, allowing efficient data retrieval.  
It:
- Stores data in a fixed-size array.
- Uses a **Hash Function** to compute an index for each key.

---

## **Hash Functions**

A **Hash Function** converts keys into fixed-size values called hashes. For example:
```python
def simple_hash(key: str, size: int) -> int:
    return len(key) % size
```

### **Attributes of a Good Hash Function**:
1. **Consistency**: Same key always produces the same hash.
2. **Efficiency**: Quick to compute.
3. **Low Collision Probability**: Reduces chances of multiple keys mapping to the same index.
4. **Uniform Distribution**: Spreads values evenly across the array.

---

## **How Hashmaps Work**

You can explore a detailed visualization of how Hashmaps work, including key-value storage and collision resolution, on **[Diagrams](https://docs.google.com/presentation/d/1pSm8f9GANBhejZog1w_Fn65BVvXoLxVVBA4PtLlTW3w/edit?usp=sharing)** 
                                                       
---

## **Handling Collisions**

Collisions occur when two keys generate the same hash. Hashmaps resolve collisions using strategies like:

### **Separate Chaining**
- **How it Works**: Store a **list** at each index to handle multiple values.
- Example:
  - "John" and "Anne" both hash to `4`.
  - Instead of overwriting, store them as:
    ```
    Index 4 -> [("John", 28), ("Anne", 19)]
    ```

### **Open Addressing**
- **How it Works**: Store all data in the same array. When a collision occurs:
  - Find the next empty slot and store the new key-value pair.
  - Variants include:
    - **Linear Probing**: Sequentially search for the next available slot.
    - **Quadratic Probing**: Use a quadratic jump (e.g., `i^2`) to find the next slot.
    - **Double Hashing**: Use a second hash function to determine the step size.

Explore these techniques in action on **[VisuAlgo - Hash Table](https://visualgo.net/en/hashtable)**.

---

## **Efficiency**

- **Average Time Complexity**:
  - Insert, Delete, Lookup: **O(1)** (with a good hash function).
- **Worst-Case Time Complexity**:
  - Insert, Delete, Lookup: **O(n)** (when all keys collide).

Dynamic hashmaps, like Python's `dict`, resize automatically, maintaining efficient operations.

---

## **Hashmap Implementations in Python**

Python's `dict` provides a hashmap implementation with dynamic resizing.  
**Example**:
```python
# Initialize a hashmap
data = {"John": 28, "Anne": 19}

# Access a value
print(data["John"])  # Output: 28

# Add a new key-value pair
data["Richard"] = 32

# Remove a key-value pair
del data["Anne"]
```

---

## **Key Points**
- Hashmaps map **keys** to **values** for efficient storage and retrieval.
- Collisions are resolved using **Separate Chaining** or **Open Addressing**.
- Python's `dict` provides a dynamic and efficient implementation.

---

## **Example Code Snippets**

### Counting Frequencies in an Array
```python
from typing import Dict, List

def get_counter(arr: List[int]) -> Dict[int, int]:
    counter: Dict[int, int] = {}
    for num in arr:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    return counter

# Example usage
array = [1, 2, 2, 3, 1, 4, 2]
print(get_counter(array))
# Output: {1: 2, 2: 3, 3: 1, 4: 1}
```

---

## **Solved Problems**

Below are links to solved problems on hashmaps:

| Problem Name               | Difficulty | Solution Link                                      |
|----------------------------|------------|--------------------------------------------------|
| Count Frequencies          | Easy       | [Count Frequencies Solution](problems/count_freq.py) |
| Two Sum                    | Easy       | [Two Sum Solution](problems/two_sum.py)          |
| Longest Substring Without Repeating | Medium     | [Longest Substring Solution](problems/longest_substring.py) |

---
