def are_you_playing_banjo(name: str) -> str:
    """
    Determines if a person plays banjo based on the first letter of their name.
    
    If the name starts with 'R' or 'r', the person plays banjo.
    Otherwise, they do not.
    
    Args:
        name (str): The name of the person.
        
    Returns:
        str: A message indicating whether they play banjo or not.
    """
    
    # Check if the first character (index 0) is 'R' or 'r'
    # We use .lower() to handle both cases efficiently in one check
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

# Example Usage
if __name__ == "__main__":
    print(are_you_playing_banjo("Rami"))    # Output: Rami plays banjo
    print(are_you_playing_banjo("ali"))     # Output: ali does not play banjo
    print(are_you_playing_banjo("Robert"))  # Output: Robert plays banjo