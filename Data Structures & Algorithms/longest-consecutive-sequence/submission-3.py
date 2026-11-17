class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums) #题目要求On
        max_length = 0
        for num in nums:
            if num - 1 not in nums_set: #如果在nums查找，list查找会变On2
                new_start = num
                length = 1
                while new_start + 1 in nums_set:
                    new_start += 1
                    length += 1
                max_length = max(max_length, length)
                
        return max_length

            
        

        