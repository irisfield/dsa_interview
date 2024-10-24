class Solution:
    """15. 3Sum"""
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # time O(n log n), space O(n)

        for i in range(len(nums)):  # time O(n)
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate for the first element
            l, r = i + 1, len(nums) - 1
            while l < r:  # time O(n^2)
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])  # space O(k)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1  # skip duplicate for the second element
        """
        Time complexity is O(n^2), due to the nested loops.
        Space complexity is O(n), as Timsort uses extra space for temporary storage.
        """
        return res
