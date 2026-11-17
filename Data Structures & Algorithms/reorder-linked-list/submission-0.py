# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # locate the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast. next.next

        # reverse the ssecond half part of the linked list
        pre = None
        cur = slow.next
        slow.next = None
        
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt 

        # merge the two by zipping them
        first, second = head, pre

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2













        