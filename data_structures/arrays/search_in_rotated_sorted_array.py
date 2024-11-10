class Solution:
    """33. Search in Rotated Sorted Array"""

    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:  # right sorted porition
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        """
        The time complexity is O(log n) because it is a binary search.
        The space complexity is O(1) as no additional memory is used.
        """
        return -1

# print(Solution().search([0, 1, 2, 3, 4], 2))
# print(Solution().search([3, 4, 0, 1, 2], 1))
print(Solution().search([4,5,6,7,0,1,2], 2))
