# Two Pointers

The **Two Pointers** technique is a common algorithmic approach often used to solve problems involving iterable data structures like arrays or linked lists. It involves using two pointers that traverse the structure independently or dependently, reducing the time complexity of problems that might otherwise require nested loops.

This method is versatile and is frequently employed in coding interviews for efficient problem-solving.

---

## **Table of Contents**

1. [Introduction to Two Pointers](#introduction-to-two-pointers)  
2. [How Two Pointers Work](#how-two-pointers-work)  
3. [Classifications of Two Pointer Problems](#classifications-of-two-pointer-problems)  
   - [Same Direction](#same-direction)  
   - [Opposite Direction](#opposite-direction)  
   - [Sliding Window](#sliding-window)  
4. [Non-array Applications](#non-array-applications)  
5. [Why Use Two Pointers?](#why-use-two-pointers)  
6. [Example Code Snippets](#example-code-snippets)  
7. [Solved Problems](#solved-problems)  

---

## **Introduction to Two Pointers**

The **Two Pointers** technique uses two variables (pointers) to traverse a data structure. It is often employed to:

- Solve problems more efficiently (typically reducing time complexity from **O(n²)** to **O(n)**).  
- Perform operations like searching, partitioning, and cycle detection.  

---

## **How Two Pointers Work**

Two pointers operate by following these general principles:

1. **Initialization**: Set the pointers at specific positions (start, end, or specific indices).  
2. **Condition**: Use logic to decide how and when to move the pointers.  
3. **Processing**: Perform operations on the elements referenced by the pointers.  
4. **Termination**: End the process when a condition (e.g., array traversal completion) is met.  

---

## **Classifications of Two Pointer Problems**

### **Same Direction**

In these problems, both pointers move in the same direction.  
**Example**: [Remove Duplicates](problems/remove_duplicates.py).  
- One pointer processes all elements, while the other keeps track of the updated array.  
- The time complexity is **O(n)** since each pointer moves linearly.

Below is a helpful visualization of same direction two-pointers operations [Two pointers map](https://docs.google.com/presentation/d/1ZqgNOK4MlCYKYiTtkCv44ShFnTuVoFNwdsNjzBbqLuo/edit?usp=sharing):


---

### **Opposite Direction**
Here, the pointers move towards each other from opposite ends.  
**Example**: [Two Sum (Sorted)](problems/two_sum_sorted.py).  
- Use this approach for problems where the order of elements matters, such as finding pairs with specific sums.  
- The condition determines whether to move the left or right pointer, ensuring linear traversal.

---

### **Sliding Window**
A variation of the same direction approach, where a "window" spans elements between two pointers.  
**Example**: [Longest Substring Without Repeating Characters](problems/longest_substring.py).  
- Efficiently tracks subsets of elements, maintaining properties like size or sum.  
- Insert/remove operations update cumulative results without recomputing the window.

---

## **Non-array Applications**

Two Pointers are not limited to arrays and can be applied to other iterable data structures like linked lists.  
**Example**: [Floyd's Cycle Detection](problems/floyd_cycle.py) (Happy Number problem).  
- The fast pointer moves two steps while the slow pointer moves one step to detect cycles efficiently.

---

## **Why Use Two Pointers?**

Two Pointers often provide a more efficient solution than naive approaches by:

1. **Reducing Time Complexity**: From **O(n²)** (nested loops) to **O(n)** or **O(n log n)**.  
2. **Linear Traversals**: Processes the data structure in a single pass.  
3. **Versatility**: Applies to a wide range of problems, from arrays to linked lists and even graphs.

---

## **Example Code Snippets**

### **Same Direction Example**
**Problem**: Remove Duplicates  
```python
def remove_duplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

---

### **Opposite Direction Example**
**Problem**: Two Sum (Sorted)  
```python
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

---

### **Sliding Window Example**
**Problem**: Longest Substring Without Repeating Characters  
```python
def longest_substring(s):
    char_set = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

---

## **Solved Problems**

| Problem Name                       | Difficulty | Solution Link                                       |
|------------------------------------|------------|---------------------------------------------------|
| Remove Duplicates                  | Easy       | [Remove Duplicates Solution](problems/remove_duplicates.py) |
| Two Sum (Sorted)                   | Easy       | [Two Sum Solution](problems/two_sum_sorted.py)    |
| Longest Substring Without Repeating Characters | Medium     | [Longest Substring Solution](problems/longest_substring.py) |

---