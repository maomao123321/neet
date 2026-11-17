# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxPath = float("-inf")

        def dfs(node):
            nonlocal maxPath   # ✅ 告诉Python：用外层定义的 maxPath，不要新建
            if not node:
                return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            cur_sum = left + right + node.val
            maxPath = max(maxPath, cur_sum)  #全局最大（某个节点和他的左右分支）
            return node.val + max(left, right) 
            # return是递归「往上传递结果」: 每个节点返回“能向父节点提供的最大单边路径和” (当前节点要和父节点连成一个路径的话，只能要么连上节点的左分支，要么右分支，不可能左右都连上)
        dfs(root)
        return maxPath
        




        