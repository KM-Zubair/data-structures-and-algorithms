# Arrays

This section covers essential concepts, operations, and complexities related to arrays in Python.

---

## **Table of Contents**
1. [Python Lists as Arrays](#python-lists-as-arrays)
2. [Indexing in Python](#indexing-in-python)
3. [Common Operations and Their Complexities](#common-operations-and-their-complexities)
4. [Key Points](#key-points)
5. [Example Code Snippets](#example-code-snippets)
6. [Solved Problems](#solved-problems)
---

## **Python Lists as Arrays**
- Python's `list` is internally implemented as a dynamic array.
- Accessing an element by its index has a time complexity of **O(1)**.

---

## **Indexing in Python**
1. **Negative Indices**:
   - Negative indices allow reverse access to list elements.
   - Example:
     ```python
     a = [1, 2, 3]
     print(a[-1])  # Output: 3
     ```

2. **Subarray Slicing**:
   - Slicing indices are **left-inclusive** and **right-exclusive**.
   - Examples:
     ```python
     a = [0, 10, 20, 30, 40, 50]
     subarray = a[2:5]  # Elements from index 2 to index 4
     print(subarray)  # Output: [20, 30, 40]
     ```

3. **Shorthand for Slicing**:
   - **From the Start**:
     ```python
     subarray = a[:2]  # Elements up to index 1
     print(subarray)  # Output: [0, 10]
     ```
   - **To the End**:
     ```python
     subarray = a[2:]  # Elements from index 2 onward
     print(subarray)  # Output: [20, 30, 40, 50]
     ```

---

## **Common Operations and Their Complexities**

| Operation              | Time Complexity | Notes                                              |
|------------------------|-----------------|----------------------------------------------------|
| Access (by index)      | **O(1)**        | Direct access using index, e.g., `a[i]`.          |
| Append (push)          | **O(1)** (avg)  | Amortized constant time; resizing may take **O(n)**. |
| Insert (at a position) | **O(n)**        | Shifts elements to make space.                    |
| Delete (pop by index)  | **O(n)**        | Shifts elements to fill the gap after removal.    |
| Delete (pop last)      | **O(1)**        | Removing the last element without shifting.       |
| Iteration              | **O(n)**        | Looping through all elements.                     |
| Slicing                | **O(k)**        | Proportional to the size of the slice `k`.        |
| Search (unsorted)      | **O(n)**        | Linear search to find the element.                |
| Search (sorted)        | **O(log n)**    | Binary search (if the array is sorted).           |
| Sorting                | **O(n log n)**  | Using Python's `sorted()` or `.sort()` methods.   |

---


## **Key Points**
- **Dynamic resizing**: When appending, Python lists may resize, requiring **O(n)** to allocate new memory and copy elements.
- **Efficient access**: Use indices for O(1) access or modification.

---

## **Example Code Snippets**

#### Access by Index:
```python
a = [1, 2, 3, 4, 5]
print(a[2])  # Output: 3
```

#### Append and Pop:
```python
a = [1, 2, 3]
a.append(4)  # a becomes [1, 2, 3, 4]
a.pop()      # a becomes [1, 2, 3]
```

#### Slicing:
```python
a = [10, 20, 30, 40, 50]
print(a[:3])  # Output: [10, 20, 30]
print(a[2:])  # Output: [30, 40, 50]
```

---


## **Solved Problems**
Below are links to solved array-related problems with explanations:

| Problem Name              | Difficulty | Solution Link                                   |
|---------------------------|------------|-----------------------------------------------|
| Two Sum                   | Easy       | [Two Sum Solution](problems/two_sum.py)       |
| Maximum Subarray          | Medium     | [Maximum Subarray](problems/max_subarray.py)  |
| Container With Most Water | Medium     | [Container With Most Water](problems/container_with_most_water.py) |
| Merge Intervals           | Medium     | [Merge Intervals](problems/merge_intervals.py) |

---