# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}

        def dfs(cur):
            # if alrealy clone, just return
            if cur in old_to_new:
                return old_to_new[cur]

            # clone current node first without neighbours
            copy = Node(cur.val)  # Node()是创建一个新的节点对象，它有两个属性:val和neighbours
            old_to_new[cur] = copy

            # then clone it's neighbors
            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)  # 从给定的起点开始 DFS 克隆
        


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