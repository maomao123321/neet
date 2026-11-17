class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_area = float('-inf')
        while left < right:
            cur_height = min(height[left], height[right])
            cur_width = right-left
            cur_area = cur_height * cur_width
            max_area = max(max_area, cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area