
'''
一、树的定义: 一个无向图是树，当且仅当：
1. 边数 = n - 1: len(edges) != n-1
2. 无环(acyclic): all nodes are not in visited
3. 连通(connected): 
return len(visited) == n 所有节点都访问到了 → 图连通
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 如果边的数量不是 n - 1，直接返回 False
        if len(edges) != n - 1:
            return False
        
        # 建立邻接表
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:  # 确保acyclic
                return False  # 有环：访问到一个已经访问过、但不是从我来的节点
            visited.add(node)
            for nei in graph[node]:
                if nei == parent: # 跳过回到上一个节点的反向边，避免误判为环或死循环。
                    continue
                if not dfs(nei, node):  # 如果某个子路径发现问题（例如遇到环），立刻返回 False
                    return False
            return True
        
        # 从0开始DFS，判断是否无环
        return dfs(0, -1) and len(visited) == n  # 最终能否访问完所有节点？== 图联通
