from typing import Optional

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Adds two numbers represented by linked lists where digits are stored in reverse order.
    
    Args:
        l1 (ListNode): Head of the first linked list.
        l2 (ListNode): Head of the second linked list.
        
    Returns:
        ListNode: Head of the resulting linked list representing the sum.
    """
    
    # Dummy head simplifies the logic for creating the new list
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    # Continue as long as there are nodes in l1 or l2, or a remaining carry
    while l1 or l2 or carry:
        # Get values from current nodes, default to 0 if node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and new carry
        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        new_digit = total_sum % 10
        
        # Create new node and move the current pointer
        current.next = ListNode(new_digit)
        current = current.next
        
        # Move l1 and l2 pointers forward if possible
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy_head.next

# Note: Testing linked lists usually requires a helper function 
# to convert lists to/from ListNode objects.