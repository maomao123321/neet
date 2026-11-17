class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

# store the results of the repeated work in an array.
        prefix = 1
        for i in range(n):
            res[i] = prefix   #先在不乘以本身的情况下更新prefix
            prefix *= nums[i] #然后再乘以本身

        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= suffix   #先在不乘以本身的情况下更新suffix
            suffix *= nums[i]  #然后再乘以本身
        
        return res



