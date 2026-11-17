# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    
    # 内层递归检查找到的树是否相同
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 外层递归找大树用来比较的起始点
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False
    # 1) 当前节点作为根，是否和 subRoot 完全一样？
        if self.isSameTree(root, subRoot):
            return True
    # 2) 不是，就去大树的左右子树继续找    
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        

        