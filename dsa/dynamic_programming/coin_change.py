class Solution:
    """322. Coin Change"""

    def coinChange(self, coins: list[int], amount: int) -> int:
        """Bottom-Up Dynamic Programming"""
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        """
        The time complexity is O(amount * n), where amount is the target
        value and n is the number of coins. This is because for each
        value from 1 to amount, the algorithm iterates over all n coins.

        The space complexity is O(amount), as the dp array requires
        storage proportional to the amount to keep track of the minimum
        coins needed for each intermediate value.
        """
        return dp[amount] if dp[amount] != float("inf") else -1

    def coinChange(self, coins: list[int], amount: int) -> int:
        """Top-Down Dynamic Programming"""
        memo = {}

        def dfs(amount):
            if amount == 0:  # no coins needed for 0 amount
                return 0
            if amount < 0:  # not possible to make negative amount
                return -1

            if amount in memo:
                return memo[amount]

            num_coins = float("inf")

            for coin in coins:
                res = dfs(amount - coin)
                if res != -1:
                    num_coins = min(num_coins, res + 1)

            memo[amount] = num_coins if num_coins != float("inf") else -1
            return memo[amount]

        """
        The time complexity is O(amount * n), where amount is the target
        value and n is the number of coins. This complexity arises
        because the memoization ensures each subproblem is solved only
        once, and there are amount states with at most n choices per
        state.

        The space complexity is O(amount), as the memoization table (memo)
        requires storage proportional to the amount, and the recursion
        stack can go up to the depth of amount in the worst case.
        """
        return dfs(amount)
