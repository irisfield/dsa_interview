class Solution:
    """983. Minimum Cost for Tickets"""
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        # decision tree
        dp = {}  # memoization
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
                dp[i] = min(dp[i], cost + dfs(j))  # space O(n)

            return dp[i]
        """
        The time complexity is O(38 * n):
        - There are n days and 1 + 7 + 30 total days worth of tickets
        The space space complexity is O(n):
        - The hash map stores results of previously computed states.
        - The
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
        The time complexity is O(38 * n):
        - There are n days and 1 + 7 + 30 total days worth of tickets
        The space space complexity is O(n):
        - The hash map stores results of previously computed states.
        """
        return dp[0]
