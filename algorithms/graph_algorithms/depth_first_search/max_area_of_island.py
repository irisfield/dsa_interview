class Solution:
    """695. Max Area of Island"""

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                grid[r][c] == 0 or (r, c) in visit):
                return 0

            visit.add((r, c))  # O(n * m) space

            return (1 + dfs(r + 1, c)
                      + dfs(r - 1, c)
                      + dfs(r, c + 1)
                      + dfs(r, c - 1))

        area = 0
        for r in range(ROWS):  # O(n * m) time
            for c in range(COLS):
                area = max(area, dfs(r, c))

        """
        Small optimization:
        Keep track of the visited positions by marking the grid
        instead of using a set. This reduces memory usage.

        The time complexity is O(n * m), as each cell is visited exactly once.
        The memory complexity is O(n * m) due to the set used for
        tracking visited positions and the recursion stack.
        """
        return area
