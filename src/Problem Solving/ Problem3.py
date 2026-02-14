from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Finds two indices such that the numbers at these indices add up to the target.
    
    This implementation uses a hash map (dictionary) to achieve O(n) time complexity.
    
    Args:
        nums (List[int]): An array of integers.
        target (int): The integer target sum.
        
    Returns:
        List[int]: The indices of the two numbers that add up to target.
    """
    
    # Dictionary to store the value as key and its index as value
    # Format: {number_value: index}
    prev_map = {} 
    
    for i, n in enumerate(nums):
        # Calculate the required number (complement) to reach the target
        diff = target - n
        
        # If the complement exists in our map, we found the solution
        if diff in prev_map:
            return [prev_map[diff], i]
        
        # Otherwise, store the current number and its index in the map
        prev_map[n] = i
        
    return [] # This line will theoretically never be reached based on constraints

# Example Usage
if __name__ == "__main__":
    nums_input = [2, 7, 11, 15]
    target_input = 9
    print(f"Indices: {two_sum(nums_input, target_input)}")
    # Output: [0, 1]