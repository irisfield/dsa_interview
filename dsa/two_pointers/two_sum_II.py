class Solution:
    """167. Two Sum II - Input Array Sorted"""

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """The solution must use constant extra space."""
        l, r = 0, len(nums) - 1
        while l < r:  # time O(n)
            total = nums[l] + nums[r]
            if  total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]  # 1-indexed array
        """
        Time complexity is O(n), as each element is processed exactly once.
        Space complexity is O(1), as no data structures were utilized.
        """
        return []  # a solution is guaranteed
