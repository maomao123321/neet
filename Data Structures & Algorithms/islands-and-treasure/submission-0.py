'''
不是从陆地找宝藏，而是从宝藏往外扩散。这叫 Multi-source BFS
在 BFS 中同时从所有源点（宝藏）出发，就能保证每个陆地被第一次访问时一定是最短距离。
'''
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
    
        dq = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dq.append((i,j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while dq:
            x,y = dq.popleft()
            for dx, dy in directions:
                nx,ny = x+dx, y+dy
                if not (0<=nx<m and 0<=ny<n):
                    continue
                if grid[nx][ny] == -1:
                    continue 
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 2147483647:
                    grid[nx][ny] = grid[x][y] + 1
                    dq.append((nx,ny))
                


