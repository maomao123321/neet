from collections import deque
#双端队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            # right end：只要新来的旧的大，就除旧迎新，连环弹出，让队列永远递减，队首最大
            while dq and nums[dq[-1]] <= nums[i]:  
                dq.pop()
            dq.append(i)

            # left end
            if dq[0] < i-k+1: #窗口范围是 [i - k + 1, i]
                dq.popleft()
            
            if i >= k-1: #表示窗口已经形成
                result.append(nums[dq[0]])
            
        return result
            
            

                
        



        