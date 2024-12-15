class Solution:
    """695. Max Area of Island"""

    # Recrusive DFS
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
        Keep track of the visited cells by marking the grid
        instead of using a set. This reduces memory usage.

        The time complexity is O(n * m), as each cell is visited exactly once.
        The memory complexity is O(n * m) due to the set used for
        tracking visited cells and the recursion stack.
        """
        return area

    # Iterative BFS/DFS
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == 0):
                return 0

            q = deque()
            q.append((r, c))
            visit.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            area = 1
            while q:
                # Changing q.popleft() to q.pop() will convert this
                # iterative BFS into an iterative DFS solution.
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1 and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
                        area += 1
            return area

        area = 0
        for r in range(ROWS):  # O(n * m) time
            for c in range(COLS):
                area = max(area, bfs(r, c))

        """
        The time complexity is O(n * m), as each cell is visited exactly once.
        The memory complexity is O(n * m) due to the set used for
        tracking visited cells, and the queue needed for BFS/DFS.
        """
        return area
