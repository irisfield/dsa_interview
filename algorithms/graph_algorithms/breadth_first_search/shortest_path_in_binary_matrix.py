class Solution:
    """1091. Shortest Path in Binary Matrix"""

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        Please note that Breadth-First Search always give
        the shortest path in an unweighted graph. If the graph is
        weighted (i.e., edges have weights), BFS does not guarantee the
        shortest path, because it treats all edges as having equal
        weight. In this case, algorithms like Dijkstra's algorithm or
        Bellman-Ford are more suitable for finding the shortest path.

        For this problem, modifying the grid is allowed. So instead of
        using a set to keep track of visited cells, modify the grid.

        The time complexity is O(n^2), as this a n x n grid.
        The space complexity is O(n^2), as the queue can hold all n^2 cells.
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        from collections import deque
        N = len(grid)  # this is an N x N grid
        q = deque([(0, 0, 1)])  # r, c, length
        grid[0][0] = 1  # mark as visited

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]
        while q:
            r, c, length = q.popleft()

            if (r, c) == (N - 1, N - 1):
                return length

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (0 <= row < N and 0 <= col < N and not grid[row][col]):
                    grid[row][col] = 1  # mark as visited
                    q.append((row, col, length + 1))
        return -1
