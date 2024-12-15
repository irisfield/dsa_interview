class Solution:
    """63. Unique Paths II"""

    from collections import deque
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        # If the starting or ending position is blocked, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        # Initialize the memoization table
        memo = [[0] * COLS for _ in range(ROWS)]
        memo[0][0] = 1  # Starting point has 1 way to be reached

        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()

            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = dr + r, dc + c
                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    obstacleGrid[r][c] == 0):
                    # If the cell has not been visited
                    if memo[nr][nc] == 0:
                        q.append((nr, nc))

                    # Add the number of ways to reach (r, c) to (nr, nc)
                    memo[nr][nc] += memo[r][c]

        """
        The time complexity is O(m * n). Each cell in the grid is
        processed at most once, and for each cell, the operations
        (checking neighbors and updating the memoization table) take
        constant time.

        The space complexity is O(m * n). The memoization table and the
        queue for BFS can store up to all cells in the grid.
        """
        return memo[ROWS - 1][COLS - 1]


    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        memo = {}

        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                obstacleGrid[r][c] == 1):
                return 0

            if (r, c) == (ROWS - 1, COLS - 1):
                return 1

            if (r, c) not in memo:
                memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)

            return memo[(r, c)]

        """
        The time complexity is O(m * n). In the worst case, every cell
        is visited once. With memoization, each cell is computed only
        once, so the time complexity is proportional to the number of
        cells in the grid.

        The space complexity is O(m * n) due to the memoization table,
        which stores the number of unique paths for each cell.
        Additionally, there is space required for the recursion stack,
        which can go as deep as the grid's dimensions
        """
        return dfs(0, 0)
