class Solution:
    """33. Search in Rotated Sorted Array"""

    def search(self, nums: list[int], target: int) -> int:
        """
        1. Divide the array into a right and left sorted portion.
        2. Check if the target is or is not in the left sorted portion.
        3. Check if the target is or is not in the right sorted portion
        4. Change the pointers depending on the above conditions.
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:  # left sorted portion
                if target > nums[mid] or target < nums[l]:
                    # If the target is not in the left sorted porition
                    l = mid + 1
                else:
                    # If the target is in the left sorted porition
                    r = mid - 1
            else:  # right sorted portion
                if target < nums[mid] or target > nums[r]:
                    # If the target is not in the right sorted porition
                    r = mid - 1
                else:
                    # If the target is in the right sorted porition
                    l = mid + 1
        """
        The time complexity is O(log n) as this is a binary search.
        The space complexity is O(1) as no additional memory is used.
        """
        return -1
