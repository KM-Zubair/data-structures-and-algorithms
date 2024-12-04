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