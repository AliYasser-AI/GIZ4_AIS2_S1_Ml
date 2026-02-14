from typing import List

def search_insert(nums: List[int], target: int) -> int:
    """
    Finds the index of the target in a sorted array, or the index where it 
    would be inserted to maintain sorted order.
    
    Complexity:
        Time: O(log n) - Binary Search approach.
        Space: O(1) - Constant space used.
        
    Args:
        nums (List[int]): Sorted list of distinct integers.
        target (int): Value to search for or insert.
        
    Returns:
        int: The index of the target or its potential insertion point.
    """
    
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Case 1: Target found
        if nums[mid] == target:
            return mid
        
        # Case 2: Target is in the right half
        elif nums[mid] < target:
            low = mid + 1
            
        # Case 3: Target is in the left half
        else:
            high = mid - 1
            
    # If not found, 'low' will be pointing to the correct insertion index
    return low

# Example Usage
if __name__ == "__main__":
    nums_test = [1, 3, 5, 6]
    print(f"Index for target 5: {search_insert(nums_test, 5)}") # Output: 2
    print(f"Index for target 2: {search_insert(nums_test, 2)}") # Output: 1
    print(f"Index for target 7: {search_insert(nums_test, 7)}") # Output: 4