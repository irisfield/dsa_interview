class Solution:
    """62. Unique Paths"""

    from collections import deque
    def uniquePaths(self, m: int, n: int) -> int:

        # Memoization table
        memo = [[0] * n for _ in range(m)]
        memo[0][0] = 1  # There is one way to get the origin

        # Initialize the queue for BFS
        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()

            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = dr + r, dc + c

                if (0 <= nr < m and 0 <= nc < n):
                    # If the cell has not been visited
                    if memo[nr][nc] == 0:
                        q.append((nr, nc))

                    # Add the numbers of way to get from (r, c) to (nr, nc)
                    memo[nr][nc] += memo[r][c]

        """
        The time complexity is O(m * n). Each cell is visited at most
        once thanks to the momoization hash map.

        The space complexity is O(m * n). The memoization table and the
        queue can store for the BFS up to the size of the matrix in the
        worst case.
        """
        return memo[m - 1][n - 1]

    def uniquePaths(self, m: int, n: int) -> int:
        # Memoization table
        memo = {}

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0

            if (r, c) == (m - 1, n - 1):
                return 1

            if (r, c) not in memo:
                memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)

            return memo[(r, c)]

        """
        The time complexity is O(m * n). Each cell is visited at most
        once thanks to the memoization hash map.

        The space complexity is O(m * n). The memoization table and the
        recursion stack can store all the cells in the matrix in the
        worst case.
        """
        return dfs(0, 0)
