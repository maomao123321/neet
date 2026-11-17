class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 1️⃣ 加入所有在 newInterval 左边、不重叠的区间
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2️⃣ 合并所有与 newInterval 重叠的区间
        # 只要当前区间的起始点 尚未 超过 newInterval 的结束点，就意味着重叠或接触
        while i < n and intervals[i][0] <= newInterval[1]: #！！！！！！
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # 3️⃣ 加入合并后的 newInterval：合并要等到重叠区间全处理完，再把最终的合并结果加进去。
        res.append(newInterval)

        # 4️⃣ 加入所有在右边的区间
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
