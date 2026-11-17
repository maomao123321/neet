# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 先让agent检查base case
        if not p and not q:   
            return True
        if not p or not q or p.val != q.val:
            return False
        
        # 派出左右分身去检查
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
        #return True if left and right else False


        
        
        