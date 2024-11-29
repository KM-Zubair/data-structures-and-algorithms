# Data Structures

This section covers fundamental concepts related to data structures, algorithms, and their complexities.

---

## Big O's

A summary of common Big O complexities:

- **O(1) Constant**: No loops.
- **O(log N) Logarithmic**: Typically searching algorithms like Binary Search when data is sorted.
- **O(n) Linear**: Single loops, iterating through `n` items.
- **O(n log(n)) Log Linear**: Usually sorting operations.
- **O(n^2) Quadratic**: Comparing every element with every other element (e.g., two nested loops).
- **O(2^n) Exponential**: Recursive algorithms solving a problem of size `N`.
- **O(n!) Factorial**: Adding a loop for every element.

### Notes:
- Iterating through half a collection is still **O(n)**.
- Two separate collections result in **O(a * b)**.

![Big O names with description](images/BigO-1.png "Big O Cheat Sheet")
---

## What Can Cause Time in a Function?

- Operations (`+`, `-`, `*`, `/`)
- Comparisons (`<`, `>`, `===`)
- Looping (`for`, `while`)
- Outside function calls (`function()`)
- Sorting algorithms

---

## Common Data Structure Operations

### Rule Book
1. **Always Worst Case**: Analyze based on the worst-case scenario.
2. **Remove Constants**: Ignore constant factors in complexity.
3. **Different Inputs → Different Variables**:
   - Example: O(a + b) for two separate inputs.
   - Nested loops across different inputs: O(a * b).
4. **Drop Non-Dominant Terms**: Keep the most significant term.

---

## What Causes Space Complexity?

Factors affecting space complexity:
- Variables
- Data Structures
- Function Calls
- Allocations
