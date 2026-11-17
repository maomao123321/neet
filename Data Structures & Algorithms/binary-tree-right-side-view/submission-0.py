# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 记录每一层的最右边，也就是dq[-1]
        if not root: return []         
        res = []
        dq = collections.deque([root])
        while dq:
            size = len(dq)
            the_most_right = dq[-1]         # 视图最右就是每一层的最右
            res.append(the_most_right.val)  # 一定要记住是节点的val!!!! dq里的都是节点对象而已
            for _ in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res

