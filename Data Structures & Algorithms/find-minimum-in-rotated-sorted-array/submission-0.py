class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left,right = 0, len(nums)-1

        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]: #中点大于最右,说明最小在右边
                left = mid + 1
            else:
                right = mid #右边有序，最小值很可能就是right自己或更前

        return nums[left] 

        #二分找最小值：任何时候，别把 mid 扔掉，除非 mid 明显不可能是最小值。（right = mid)