class Solution:
    """983. Minimum Cost for Tickets"""

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        # Decision tree with memoization
        dp = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float("inf")
            for day, cost in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + day:
                    j += 1
                dp[i] = min(dp[i], cost + dfs(j))  # Space complexity: O(n)

            return dp[i]

        """
        The time complexity is O(38 * n), because:
            - There are n days, and for each day, we consider 1, 7, and 30-day tickets.

        The space complexity is O(n), because:
            - The dp dictionary stores results for previously computed states.
        """
        return dfs(0)

    def mincostTicketsDP(self, days: list[int], costs: list[int]) -> int:
        dp = {}
        for i in range(len(days) - 1, -1, -1):
            dp[i] = float("inf")
            for day, cost in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + day:
                    j += 1
                dp[i] = min(dp[i], cost + dp.get(j, 0))

        """
        The time complexity is O(38 * n), because:
            - There are n days, and for each day, we consider 1, 7, and 30-day tickets.

        The space complexity is O(n), because:
            - The dp dictionary stores results for previously computed states.
        """
        return dp[0]
