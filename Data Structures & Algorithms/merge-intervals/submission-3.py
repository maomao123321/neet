class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])                 # 一定要先排序！！
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                #res[-1][0] = min(interval[0], res[-1][0]) 
                res[-1][1] = max(interval[1], res[-1][1]) # 最后更新res,而不是interval
        return res
        