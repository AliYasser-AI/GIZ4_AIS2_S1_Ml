import math

def calculate(s: str) -> int:
    """
    Evaluates a basic mathematical expression with +, -, *, and /.
    
    Handles operator precedence by using a stack. Multiplications and 
    divisions are processed immediately, while additions and subtractions
    are pushed to the stack for final summation.
    
    Args:
        s (str): The expression string.
        
    Returns:
        int: The result of the expression evaluation.
    """
    if not s:
        return 0
    
    stack = []
    current_number = 0
    last_operator = '+'
    
    # Cleaning spaces is handled during iteration to maintain O(n)
    for i, char in enumerate(s):
        # Build the multi-digit number
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        
        # If character is an operator or we reached the end of the string
        if char in "+-*/" or i == len(s) - 1:
            if last_operator == '+':
                stack.append(current_number)
            elif last_operator == '-':
                stack.append(-current_number)
            elif last_operator == '*':
                # Multiply the last number in stack with the current one
                stack.append(stack.pop() * current_number)
            elif last_operator == '/':
                # Truncate toward zero: int(a / b) in Python 3
                # Using stack.pop() / current_number handles signs correctly
                stack.append(int(stack.pop() / current_number))
            
            # Update the operator and reset the current number
            last_operator = char
            current_number = 0
            
    return sum(stack)

# Example Usage
if __name__ == "__main__":
    print(f"Result of '3+2*2': {calculate('3+2*2')}")    # Output: 7
    print(f"Result of ' 3/2 ': {calculate(' 3/2 ')}")      # Output: 1
    print(f"Result of ' 3+5 / 2 ': {calculate(' 3+5 / 2 ')}") # Output: 5