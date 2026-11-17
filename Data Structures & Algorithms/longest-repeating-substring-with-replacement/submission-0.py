class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # diff = windowSize - maxFrequencyNum = right -left + 1 - maxFre

        count = {}
        maxFre = 0
        max_length = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
# 关键：我们只追踪历史上出现过的最大频率，因为 max_length 只会增加
            maxFre = max(maxFre,count[s[right]])
            
            window_size = right -left + 1
            if window_size - maxFre > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right -left + 1)

        return max_length
                 

            

            

        