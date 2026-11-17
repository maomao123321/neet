"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 1. 处理边界条件：空图
        if not node:
            return None
        
        # 2. 哈希表：记录 visited[原节点] = 克隆节点
        visited = {}

        def dfs(original_node):
            # Base Case: 如果该节点已经访问过（克隆过），直接返回对应的克隆节点
            if original_node in visited:
                return visited[original_node]
            
            # Logic: 创建新节点（克隆值）
            clone_node = Node(original_node.val)
            
            # 关键：在遍历邻居之前，先把新节点放入哈希表
            # 这是为了防止处理环的时候死循环
            visited[original_node] = clone_node
            
            # 递归处理所有邻居

            for neighbor in original_node.neighbors:
                # 将克隆好的邻居加入当前克隆节点的邻居列表中
                clone_node.neighbors.append(dfs(neighbor))
            
            return clone_node

        return dfs(node)
        


'''      
假设图: 1 —— 2
每个节点：
node1.neighbors = [node2]
node2.neighbors = [node1]
克隆过程：
1️⃣ 看到 node1 → 创建 copy1
2️⃣ 进入 dfs(node2) → 创建 copy2
3️⃣ 把 copy2 放进 copy1.neighbors
4️⃣ 再进入 dfs(node1)，发现已经访问过，就返回 copy1
5️⃣ 把 copy1 放进 copy2.neighbors
'''