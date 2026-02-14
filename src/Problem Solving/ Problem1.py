def reverse_words(s: str) -> str:
    """
    Reverses the order of words in a given string.
    
    The function assumes that words are separated by exactly one space 
     and there are no leading or trailing spaces.
    
    Args:
        s (str): The input string containing words to be reversed.
        
    Returns:
        str: A new string with the words in the opposite order.
    """
    
    # Step 1: Split the string into a list of words using a space as the delimiter
    words = s.split(" ")
    
    # Step 2: Reverse the list using Python's slicing method [start:stop:step]
    # -1 step means we iterate from the end to the beginning
    reversed_list = words[::-1]
    
    # Step 3: Join the reversed list back into a single string with spaces
    return " ".join(reversed_list)

# Example Usage
if __name__ == "__main__":
    example_input = "The greatest victory is that which requires no battle"
    result = reverse_words(example_input)
    
    print(f"Original: {example_input}")
    print(f"Reversed: {result}")