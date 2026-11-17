# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre = None
        cur = head

        while cur:   
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        
        return pre
    
    # 存储+反转：先存储next信息，然后原地调转cur(告诉cur你怎么打电话)；
    # 更新：cur现在是已经反转好的新链表的头部。把 cur 设为新的 prev
    # 前进！：将当前指针移到我们预存的那个next上,他即将变成被操作的cur