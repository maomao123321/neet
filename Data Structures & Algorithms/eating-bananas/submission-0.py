import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / mid)

            if totalHours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left
