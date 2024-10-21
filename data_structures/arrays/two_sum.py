class Solution:
    """199. Binary Tree Right Side View"""
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, n in enumerate(nums):  # time O(n)
            complement = target - n  # value we are looking for
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[n] = i  # space O(n)
        """
        Time complexity is O(n), as each element is processed once.
        Space complexity is O(n), as the hash map can match the array's size in the worst case.
        """
        return []  # no solution
