class Solution:
    """11. Container With Most Water"""
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        bestArea = 0
        while l < r:  # time O(n)
            area = min(height[l], height[r]) * (r - l)
            bestArea = area if area > bestArea else bestArea
            # move the pointer that pointers to the lower line
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        """
        Time complexity is O(n), as each element is processed once.
        Space complexity is O(1), as no data structures were utilized.
        """
        return bestArea

assert Solution().maxProfit([1,8,6,2,5,4,8,3,7]) == 49, "Expected 49"
assert Solution().maxProfit([1,1]) == 1, "Expected 1"
