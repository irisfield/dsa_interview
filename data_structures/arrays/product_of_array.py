class Solution:
    """238. Product of Array Except Self"""
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)  # space O(n)

        prefix = 1
        for i in range(len(nums)):  # time O(n)
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):  # time O(n)
            res[i] *= postfix
            postfix *= nums[i]
        """
        Time complexity is O(n), as there are two separate passes over the list.
        Space complexity is O(1), as the result does not count as extra space.
        """
        return res

    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        res = []
        size = size
        prefix = [1] * size # space O(n)
        postfix = [1] * size # space O(n)

        for i in range(size):  # time O(n)
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] * nums[i]

        for i in range(size - 1, -1, -1):  # time O(n)
            if i == size - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i + 1] * nums[i]

        for i in range(size):  # time O(n)
            prev = 1 if i == 0 else prefix[i - 1]
            next = 1 if i == size - 1 else postfix[i + 1]
            res.append(prev * next)  # space O(n)
        """
        Time complexity is O(n), as there are two separate passes over the list.
        Space complexity is O(n) for the prefix and postfix lists.
        """
        return res
