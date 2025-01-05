class Solution:
    """46. Permutations"""

    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        if len(nums) == 1:
            return [nums.copy()]

        for _ in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            res.extend(perms)
            nums.append(n)

        """
        The time complexity is O(n!), where n is the number of elements
        in the input list. This is because there are n! permutations,
        and generating each permutation involves O(n) operations due to
        copying and appending.

        The space complexity is O(n!), as the result list stores all
        permutations, and the recursion stack can go up to O(n) levels
        deep due to the depth-first search.
        """
        return res
