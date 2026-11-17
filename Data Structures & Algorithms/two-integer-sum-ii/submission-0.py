class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        res = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]    # Return the indices (1-indexed) 
            elif numbers[left] + numbers[right] < target:
                left += 1
            else: 
                right -= 1  

        
            
        