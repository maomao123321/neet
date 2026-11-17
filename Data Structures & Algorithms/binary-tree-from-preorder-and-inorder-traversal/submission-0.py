class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 用哈希表记录每个节点在 inorder 中的位置
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0  # 当前在 preorder 的位置

        def dfs(left, right):
            nonlocal pre_idx
            if left > right:
                return None
            
            # 当前根节点的值
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # 找根节点在 inorder 中的下标
            mid = inorder_index[root_val]

            # 递归构造左右子树
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(inorder) - 1)
