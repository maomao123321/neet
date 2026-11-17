'''
这题是一个非常标准的「图 + DFS 模板」题，以后碰到：
“有几个岛？” “有几个区块？” “有几个连通部分？”
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. 建图：邻接表
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # 2. 标准 DFS：从某node出发，把和这个node连在一起的所有其他node都标记成已访问
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        # 3. 遍历所有节点，数有多少个「起点」
        res = 0
        for i in range(n):
            if i not in visited:    # 说明这是一个新的连通块的起点
                res += 1
                dfs(i)
        
        return res
