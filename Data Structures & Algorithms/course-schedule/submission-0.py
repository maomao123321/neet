from collections import deque
from typing import List, Tuple

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[Tuple[int, int]]) -> bool:
        
        # 1. 初始化数据结构
        
        # adj: 邻接表，存储 [课程 A] -> [它后续依赖的课程 B, C...]
        # adj[A] = [B, C] 表示 A 是 B 和 C 的先修课
        adj = [[] for _ in range(numCourses)]
        
        # in_degree: 存储每门课的入度（有多少先修课）
        in_degree = [0] * numCourses
        
        # 填充邻接表和入度数组
        # 依赖关系 [a, b] 表示：先上 b，才能上 a (b -> a)
        for course, prerequisite in prerequisites:
            # prerequisite -> course
            adj[prerequisite].append(course)
            in_degree[course] += 1
            
        # 2. 初始化队列：放入所有入度为 0 的课程
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                
        # 3. BFS 核心循环：消除依赖
        courses_completed = 0
        
        while queue:
            current_course = queue.popleft()
            courses_completed += 1
            
            # 遍历当前课程的所有后续课程 (消除依赖)
            for next_course in adj[current_course]:
                
                # 消除依赖：后续课程的入度减 1
                in_degree[next_course] -= 1
                
                # 4. 检查是否可以加入生产清单 (入度是否为 0)
                if in_degree[next_course] == 0:
                    queue.append(next_course)
                    
        # 5. 最终判断 (检测环)
        # 如果完成的课程数等于总课程数，则无环
        return courses_completed == numCourses