# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy
# 如果 fast 从 head 开始 → 走 n 步；如果 fast 从 dummy 开始 → 走 n+1 步        
        
        for _ in range(n+1):   # fast从dummy先走n+1步
            fast = fast.next

        while fast:           # fast和slow一起走到链表尾部
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

# fast 走 n+1 是为了制造一个间隔：fast 和 slow 相距 n+1
# 当 fast 到尾部（null），slow 就在倒数第n-1位置
        

        