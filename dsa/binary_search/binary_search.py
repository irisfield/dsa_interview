class Solution:
    """704. Binary Search"""

    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid

        """
        The time complexity of this binary search algorithm is O(log n)
        because at each iteration, the search space is halved, reducing
        the problem size logarithmically.
        """
        return -1
