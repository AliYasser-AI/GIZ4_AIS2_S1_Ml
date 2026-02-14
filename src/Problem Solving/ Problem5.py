def roman_to_int(s: str) -> int:
    """
    Converts a Roman numeral string to an integer.
    
    The logic follows the standard Roman numeral rules:
    - Addition: When a larger value precedes a smaller one (e.g., VI = 5+1 = 6).
    - Subtraction: When a smaller value precedes a larger one (e.g., IV = 5-1 = 4).
    
    Args:
        s (str): A valid Roman numeral string.
        
    Returns:
        int: The integer representation of the Roman numeral.
    """
    
    # Mapping of Roman symbols to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    length = len(s)
    
    for i in range(length):
        # Current symbol value
        current_val = roman_map[s[i]]
        
        # Check if there is a 'next' symbol and if it's larger than the current one
        if i + 1 < length and current_val < roman_map[s[i + 1]]:
            # If current is smaller than next, subtract it (e.g., IV -> -1 + 5)
            total -= current_val
        else:
            # Otherwise, add it (e.g., VI -> 5 + 1)
            total += current_val
            
    return total

# Example Usage
if __name__ == "__main__":
    print(f"MCMXCIV: {roman_to_int('MCMXCIV')}")  # Output: 1994
    print(f"LVIII: {roman_to_int('LVIII')}")      # Output: 58