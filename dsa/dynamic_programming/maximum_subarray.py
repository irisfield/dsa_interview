class Solution:
    """53. Maximum Subarray"""

    def maxSubArray(self, nums: list[int]) -> int:
        """Kadane's Algorithm"""
        maxima = max(nums)  # O(n) time

        if maxima <= 0:
            return maxima

        res = nums[0]
        cur = 0

        for n in nums:
            cur += n

            if cur < 0:
                cur = 0

            res = max(res, cur)

        """
        The time complexity is O(n) as each element is visited twice.
        The space complexity is O(1) as no data structures were used.
        """
        return res

    def maxSubArray(self, nums: list[int]) -> int:
        """Kadane's Algorithm"""
        res, ending = nums[0], nums[0]

        for i in range(1, len(nums)):
            ending = max(ending + nums[i], nums[i])
            res = max(res, ending)

        """
        The time complexity is O(n) as each element is visited once.
        The space complexity is O(1) as no data structures were used.
        """
        return res
