class Solution:
    """221. Maximal Square"""

    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # Dynamic programming - bottom up solution
        ROWS, COLS = len(matrix), len(matrix[0])
        largest = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r + 1 < ROWS and c + 1 < COLS and matrix[r][c] == "1":
                    down = int(matrix[r + 1][c])
                    right = int(matrix[r][c + 1])
                    diag = int(matrix[r + 1][c + 1])
                    matrix[r][c] = 1 + min(down, right, diag)
                largest = max(largest, int(matrix[r][c]))
        """
        The time complexity is O(m * n), where m * n is the size of the
        matrix.

        The space complexity is O(1) as the matrix is modified in place.
        """
        return largest ** 2


    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # Recursive solution - top down memoization
        ROWS, COLS = len(matrix), len(matrix[0])

        cache = {}  # map each (r, c) -> max length of square

        def helper(r, c):
            if r == ROWS or c == COLS:
                return 0

            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]

        helper(0, 0)

        """
        The time complexity is O(m * n), where m * n is the size of the
        matrix.

        The space complexity is O(m * n) because of the recursion call
        stack and the memoization table.
        """
        return max(cache.values()) ** 2
