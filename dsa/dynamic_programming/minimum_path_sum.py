class Solution:
    """64. Minimum Path Sum"""

    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dp = {}

        def dfs(r, c):
            if r == ROWS or c == COLS:
                return float("inf")

            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]

            if (r, c) in dp:
                return dp[(r, c)]

            down = dfs(r + 1, c)
            right = dfs(r, c + 1)

            dp[(r, c)] = grid[r][c] + min(down, right)

            return dp[(r, c)]

        """
        The time complexity is O(m * n). Due to the memoized recrusive
        calls each cell is processed exactly once.

        The space complexity is O(m * n). The memoization table stores
        the minimum path sum for each cell in the grid.
        """
        return dfs(0, 0)

    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
        res[ROWS - 1][COLS] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                down, right = res[r + 1][c], res[r][c + 1]
                res[r][c] = grid[r][c] + min(down, right)

        """
        The time complexity is O(m * n). Due to the memoized recrusive
        calls each cell is processed exactly once.

        The space complexity is O(m * n). The memoization table stores
        the minimum path sum for each cell in the grid.
        """
        return res[0][0]
