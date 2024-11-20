class Solution:
    """980. Unique Paths III"""

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        empty = 0  # Number of empty cells
        start = end = None

        for r in range(ROWS):  # O(m * n) time
            for c in range(COLS):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    end = (r, c)
                elif grid[r][c] == 0:
                    empty += 1

        res = 0
        visited = set()

        def dfs(r, c, walk):
            nonlocal res

            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                grid[r][c] == -1 or (r, c) in visited):
                return

            if (r, c) == end and (walk - 1) == empty:
                res += 1
                return

            visited.add((r, c))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r + dr, c + dc, walk + 1)

            visited.remove((r, c))  # backtrack

        dfs(*start, 0)
        """
        The time complexity is O(m * n * 4^(m * n)), where m and n are
        the dimensions of the grid. This accounts for the initial grid
        scan (O(m * n)) and the potentially exponential number of DFS
        calls exploring all paths through the grid. Each DFS call checks
        four possible directions (up, down, left, right) for each cell,
        leading to an exponential number of calls. Thus, the worst-case
        time complexity is O(4^(m*n)) where (m * n) is the number of
        steps from the start to the end point.

        The space complexity is O(m * n). This accounts for the visited
        set and the recursion stack which in the worse case will grow to
        the size of the grid.
        """
        return res
