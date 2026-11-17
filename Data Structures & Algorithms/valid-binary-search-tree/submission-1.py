class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 凡是 BST / 全局约束类树题， 都不能只看“父子关系”，必须“把约束一路往下传”

        def dfs(node, low, high):
            if not node: return True
            if not(low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, -float('inf'), float('inf'),)

