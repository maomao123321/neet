# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法一：利用二叉搜索树的特性
# 如果 p 和 q 都比当前节点小 → 往左走；
# 如果都比当前节点大 → 往右走；
# 否则，当前节点正好是分叉点，也就是 LCA。
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left     # p 和 q 都在左边
            elif p.val > root.val and q.val > root.val:
                root = root.right    # p 和 q 都在右边
            else:
                return root          # 分叉点 or 其中一个等于 root


# #方法二：通用法

# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         # to iterate through all nodes, and if the left and right can be found by p & q, then this node is the LCA
#         # base case:
#         if not root or root == p or root == q:
#             return root
        
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)

#         if left and right:
#             return root
#         elif left:
#             return left
#         elif right:
#             return right
#         else:
#             return None

        