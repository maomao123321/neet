class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

# 与其想着“删谁”，不如反过来想：我最多能保留多少个互不重叠的区间？

        # 1. 按 end 升序排序：
        # 我们希望当前选的区间尽量早结束，这样后面能“塞”进更多区间（典型贪心思想，和活动选择问题一样）。
        intervals.sort(key=lambda x: x[1])

        # 2. 贪心选不重叠的区间
        end = float('-inf')
        count = 0

        for s, e in intervals:
            if s >= end:  # 和前一个interval 的 end比较
                # 不重叠，可以留着这个interval
                count += 1
                end = e
            else:
                # 重叠，跳过（相当于删掉这个区间）
                continue

        # 3. 总数 - 能保留的 = 需要删除的
        return len(intervals) - count
