class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        res = []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pacific = set()
        atlantic = set()

        def dfs(x,y,visited,pre_height): # meaning of dfs: can current index go to the next required one
            if not (0<=x<n and 0<=y<m):
                return
            if (x,y) in visited:
                return
            if heights[x][y] < pre_height:
                return
            visited.add((x,y))
            for dx, dy in directions:
                nx,ny = x+dx, y+dy
                dfs(nx,ny,visited, heights[x][y])
                
        # up left down right 
        for i in range(m): # m是列数，所以是行为0，列在变
            dfs(0,i,pacific,heights[0][i])
        for j in range(n):
            dfs(j,0,pacific,heights[j][0])
        for i in range(m):
            dfs(n-1,i,atlantic,heights[n-1][i])
        for j in range(n):
            dfs(j,m-1,atlantic,heights[j][m-1])

        # 看哪些点是被两个集合都visited到的 说明这个点可以两边通
        for i in range(n):
            for j in range(m):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res


