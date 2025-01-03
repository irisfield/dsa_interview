class Solution:
    """994. Rotting Oranges"""

    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0
        rotten = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c, 0))

        if fresh == 0:
            return 0

        res = 0
        visited = set()
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        while rotten:
            for _ in range(len(rotten)):
                r, c, time = rotten.popleft()
                res = max(res, time)

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr == ROWS or
                        nc < 0 or nc == COLS or
                        grid[nr][nc] != 1 or
                        (nr, nc) in visited):
                        continue
                    else:
                        visited.add((nr, nc))
                        rotten.append((nr, nc, time + 1))
                        fresh -= 1

        """
        The time complexity is O(n * m). In the worst case, each node is
        visited at most twice, once for the initial pass to count the
        fresh oranges and populating the queue with the rotten oranges,
        and then again during the level-order traversal with BFS to rot
        all the adjacent fresh oranges.

        The space complexity is O(n * m). This accounts for the space
        required by the queue with the rotten oranges and the set for fresh
        oranges that were rotted. Memory could be optimized slightly by
        modifying the grid in place instead of using a set.
        """
        return -1 if fresh > 0 else minute


    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0
        rotten = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        if fresh == 0:
            return 0

        res = 0
        time = 0
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                r, c, time = rotten.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nr == ROWS or
                        nc < 0 or nc == COLS or
                        grid[nr][nc] != 1):
                        continue

                    grid[nr][nc] = 2
                    rotten.append((nr, nc))
                    fresh -= 1
            time += 1

        """
        The time complexity is O(n * m), where n and m are the
        dimensions of the grid. In the worse case, each cell is
        processed at most twice: once during the initial setup and once
        during the BFS traversal to rot adjacent fresh oranges.

        The space complexity is O(n * m), as the queue used for BFS can
        store up to n * m cells in the worst case, depending on the
        number of rotten oranges and their spread.
        """
        return -1 if fresh > 0 else time
