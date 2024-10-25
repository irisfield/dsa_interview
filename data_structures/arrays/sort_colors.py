class Solution:
    """75. Sort Colors"""
    def sortColors(self, nums: list[int]) -> None:
        """Single pass two pointers solution"""
        i, l, r = 0, 0, len(nums) - 1
        while i <= r:  # time O(n)
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r, i = r - 1, i - 1
            i += 1

    def sortColors2(self, nums: list[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        # Bucket sort - time O(n)
        bucket = {}
        for i in range(len(nums)):  # time O(n)
            bucket[nums[i]] = 1 + bucket.get(nums[i], 0)

        i, j = 0, 0
        while i < len(nums):  # time O(n)
            if j in bucket and bucket[j] > 0:
                nums[i] = j
                bucket[j] -= 1
                i += 1
            else:
                j += 1
