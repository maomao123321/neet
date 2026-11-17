class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # 1. Initialization
        slow = head
        fast = head
        
        # 2. Cycle Detection Loop
        # Check for fast and fast.next to prevent NullPointerExceptions 
        while fast and fast.next:
            
            # Move the pointers
            slow = slow.next
            fast = fast.next.next
            
            # 3. Meeting Point Check
            if slow == fast:
                # Cycle found!
                return True
                
        # 4. Termination
        # If the loop finishes, the fast pointer reached the end (None)
        return False