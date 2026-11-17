from typing import Optional, List

# 假设 ListNode 结构已定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. 初始化虚拟头节点 (Dummy Head)
        dummy = ListNode()
        tail = dummy # tail 是工作指针，始终指向合并后的链表的末尾
        
        # 2. 比较循环：当两个链表都还有节点时
        while l1 and l2:
            if l1.val < l2.val:
                # 选取 l1 的节点
                tail.next = l1
                l1 = l1.next
            else:
                # 选取 l2 的节点
                tail.next = l2
                l2 = l2.next
            
            # 移动尾指针到新连接的节点上
            tail = tail.next 
            
        # 3. 收尾：连接剩下的部分
        # 剩下的非空链表部分一定是有序的，直接连接
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        # 4. 返回结果：跳过虚拟头节点
        return dummy.next