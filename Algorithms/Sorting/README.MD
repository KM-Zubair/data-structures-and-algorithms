# Sorting Algorithms in Python

This repository explores fundamental sorting algorithms with Python implementations. It provides insights into the concepts, time complexity, stability, and in-place properties of popular sorting methods.

---


## Sorting Algorithm Complexity

<img src="https://lamfo-unb.github.io/img/Sorting-algorithms/Complexity.png" alt="Sorting Algorithms Complexity Visualization" width="600">

---

## Overview

Sorting is a fundamental operation in computer science, essential for many algorithms and real-world applications. This repository covers:
- Key terms like **time complexity**, **stability**, and **in-place sorting**.
- Implementations of core sorting algorithms.
- Examples and explanations to help you understand the mechanics of each method.

---

## Why Avoid Using `sort()`?

`sort()` shouldn't be used in some cases because it can have higher memory overhead. For instance:
- `sorted()` creates a new sorted list, which increases memory usage.
- It may require additional temporary storage during the sorting process.

In memory-constrained environments, in-place or custom sorting algorithms might be preferred.

---

## Included Algorithms

### 1. **Insertion Sort**
- **Concept**: Sorts elements by repeatedly "inserting" them into the correct position in a sorted sublist.
- **Complexity**: \(O(n^2)\)
- **Properties**: Stable, In-place.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

---

### 2. **Selection Sort**
- **Concept**: In selection sort, the smallest element in the unsorted part of the list is repeatedly selected and swapped with the first unsorted element. This process divides the list into a "sorted" and "unsorted" portion, growing the sorted part one element at a time.
- **Time Complexity**: \(O(n^2)\)
- **Space Complexity**: \(O(1)\)
- **Properties**: Not stable, In-place.

Check the diagram below to understand it step by step **[Diagram](https://docs.google.com/presentation/d/1o3dLETNTQzlBCUm6TCK7StOA1YUg8Tr-RpcI3r2VfP4/edit?usp=sharing)** 

```python
from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    # Iterate through the entire list
    for i in range(len(arr)):
        # Assume the current index has the minimum value
        min_idx = i
        
        # Find the minimum element's index from the rest of the list
        for j in range(i + 1, len(arr)):
            # Update min_idx if a smaller element is found
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage
if __name__ == "__main__":
    # Read input as a list of integers
    numbers = list(map(int, input().split()))
    
    # Sort the numbers
    sorted_numbers = selection_sort(numbers)
    
    # Print the sorted numbers
    print(" ".join(map(str, sorted_numbers)))

```

---

### 3. **Bubble Sort**
- **Concept**: Repeatedly swaps adjacent elements if they are in the wrong order. The largest element "bubbles" to the top in each iteration.
- **Complexity**: \(O(n^2)\)
- **Properties**: Stable, In-place.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

---

## Key Sorting Concepts

- **Stability**: Maintains the relative order of elements with equal values.
- **In-Place Sorting**: Requires minimal extra memory.
- **Time Complexity**: Measures the efficiency of algorithms as input size grows.

---


