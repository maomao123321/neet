from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. 初始化图和入度表
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        # 建立邻接表
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        
        # 2. 初始化队列（所有入度为0的节点）
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        # 3. 拓扑排序 BFS
        while queue:
            cur = queue.popleft()
            order.append(cur)
            for next_course in adj[cur]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # 4. 检查是否存在环
        return order if len(order) == numCourses else []
