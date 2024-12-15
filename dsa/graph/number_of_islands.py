class Solution:
    """200. Number of Islands"""

    # Recursive DFS
    def numIslands(self, grid: list[list[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                grid[r][c] == "0" or (r, c) in visit):
                return 0

            visit.add((r, c))  # O(n * m) space
            return (1 + dfs(r + 1, c)
                      + dfs(r - 1, c)
                      + dfs(r, c + 1)
                      + dfs(r, c - 1))

        count = 0
        for r in range(ROWS):  # O(n * m) time
            for c in range(COLS):
                count += 1 if dfs(r, c) > 0 else 0

        """
        Small optimization:
        Keep track of the visited cells by marking the grid
        instead of using a set. This reduces memory usage.

        The time complexity is O(n * m), as each cell is visited exactly once.
        The memory complexity is O(n * m) due to the set used for
        tracking visited cells and the recursion stack.
        """
        return count

    # Iterative BFS/DFS
    def numIslands(self, grid: list[list[str]]) -> int:
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                # Changing q.popleft() to q.pop() will convert this
                # iterative BFS into an iterative DFS solution.
                row, col = q.popleft()
                directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and
                        grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        """
        Small optimization:
        Consider marking the visited cells directly on the grid
        (e.g. changing "1" to "0") instead of using a set.

        The time complexity is O(n * m), as each cell is visited exactly once.
        The memory complexity is O(n * m) due to the set used for
        tracking visited cells, and the queue needed for BFS/DFS.
        """
        return islands
