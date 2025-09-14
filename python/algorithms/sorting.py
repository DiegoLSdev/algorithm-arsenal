# ============================================================================
# BASIC SORTING ALGORITHMS O(n²)

    
    # Bubble Sort - Repeatedly steps through list, compares adjacent elements
    # Time: O(n²), Space: O(1)
    # Stable: Yes, In-place: Yes
    
    # Best for: Educational purposes, very small datasets
# ============================================================================

from typing import List

def bubble_sort(arr: List[int]) -> List[int]:

    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    return arr




# ============================================================================
# BASIC SORTING ALGORITHMS O(n²)

    
    # Selection Sort - Find minimum element and put it at beginning
    # Time: O(n²), Space: O(1)
    # Stable: No, In-place: Yes
    
    # Best for: Small datasets, when memory writes are expensive
# ============================================================================

def selection_sort(arr: List[int]) -> List[int]:

    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        # Find minimum element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap found minimum with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr