class Solution:
    """312. Burst Ballons"""
    def maxCoins(self, nums: list[int]) -> int:
        dp = {}
        nums = [1] + nums + [1]

        def dfs(l, r):  # O(n^2) for the unique pairs
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r):  # times O(n) for each (l, r) pair
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        """
        The time complexity is O(n^3) because:
            - There are O(n^2) unique pairs (l, r).
            - For each pair, we perform O(n) operations in the loop.

        The space complexity is O(n^2) due to:
            - The dp dictionary storing results for O(n^2) pairs.
            - Each entry takes constant space.
            - The recursive call stack can reach O(n) in depth.
            - Overall, O(n) + O(n^2) simplifies to O(n^2).
        """
        return dfs(1, len(nums) - 2)
