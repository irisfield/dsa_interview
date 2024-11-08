class Solution:
    """70. Climbing Stairs"""

    def climbStairs(self, n: int) -> int:
        # Decisions: take 1 step, take 2 steps
        # Dynamic Programming - Bottom Up
        one, two = 1, 1
        for in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
        """
        The time complexity is O(n) as each element is processed exactly once.
        The space complexity is O(1) as no data structures were utilized.
        """
        return backtrack(0, {})

    def climbStairs(self, n: int) -> int:
        # Decisions: take 1 step, take 2 steps
        # Dynamic Programming - Top Down
        def backtrack(steps, cache):
            if steps > n:
                return 0
            if steps == n:
                return 1
            if steps in cache:
                return cache[steps]
            cache[steps] = (backtrack(steps + 1, cache) +
                         backtrack(steps + 2, cache))
            return cache[steps]
        """
        The time complexity is O(n) because thanks to memoization each
        subproblem is being solved once.

        The space complexity is O(n), where n is the height of the tree
        plus the size of recursion call stack.
        """
        return backtrack(0, {})
