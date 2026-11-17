class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 初始调用：使用负无穷和正无穷来表示初始范围没有限制
        return self.isValid(root, float('-inf'), float('inf'))

    # 辅助函数：需要额外的参数来传递边界 (min_val, max_val)
    def isValid(self, node, min_val, max_val) -> bool:
        
        # 1. 终止条件 (Base Case): 到达空节点，说明该路径上的所有节点都通过了检查，返回 True
        if not node:
            return True
            
        # 2. 前置检查 或 剪枝，检查当前节点的值是否在允许的 (min_val, max_val) 范围内
        if not (min_val < node.val < max_val):
            return False
            
        # 3. 深入探索 (Recursive Calls)
        
        # A. 派分身去左子树: 左子树的所有节点必须 < node.val。因此，最大值边界更新为 node.val。
        left_valid = self.isValid(node.left, min_val, node.val)
        
        # B. 派分身去右子树: 右子树的所有节点必须 > node.val。因此，最小值边界更新为 node.val。
        right_valid = self.isValid(node.right, node.val, max_val)
        
        # 4. 整合报告：左右子树都必须有效
        return left_valid and right_valid