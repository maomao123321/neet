class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))   # 节点从 1 到 n
        
        # 带路径压缩
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa == pb:
                return [a, b]  # a 和 b 已经在同一个连通块里了，这条边多余
            parent[pa] = pb    # 否则把两块连起来


