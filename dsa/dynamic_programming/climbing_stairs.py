class Solution:
    """70. Climbing Stairs"""

    def climbStairs(self, n: int) -> int:
        """
        Dynamic Programming - Top Down Approach:
        This approach solves the problem starting from the top (target)
        and works its way down to the base cases via recursion, saving
        the results in a memoization table.

        Decisions: take 1 step or take 2 steps
        You can climb 1 or 2 steps at a time to reach the top.

        Base Cases:
        - 1 step can be reached in exactly 1 way (1 step).
        - 2 steps can be reached in 2 ways:
          1. Climbing 1 step + 1 step.
          2. Climbing 2 steps at once.
        """
        dp = { 1 : 1, 2 : 2 }  # dp[i] is the number of ways to get to i

        def dfs(i):
            if i in dp:
                return dp[i]

            dp[i] = dfs(i - 1) + dfs(i - 2)
            return dp[i]

        """
        The time complexity is O(n). Due to memoization, each subproblem
        is solved only once.

        The space complexity is O(n). Space is used for storing the
        memoized results (dp), plus the call stack for recursion.
        """
        return dfs(n)


    def climbStairs(self, n: int) -> int:
        """
        Dynamic Programming - Bottom Up:
        This approach starts from the smallest subproblems (base cases)
        and iteratively solve all subproblems until reaching the target
        (top).


        Decisions: take 1 step, take 2 steps
        """
        one, two = 1, 1
        for in range(n - 1):
            temp = one
            one = one + two
            two = temp
        """
        The time complexity is O(n) as each element is processed once.
        The space complexity is O(1) as no data structures were used.
        """
        return one
