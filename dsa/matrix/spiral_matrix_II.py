class Solution:
    """59. Spiral Matrix II"""

    def generateMatrix(self, n: int) -> list[list[int]]:
        if n == 1:
            return [[1]]

        res = [[0] * n for _ in range(n)]

        #   L  L     R  R
        # T 01 02 03 04
        # T 12 13 14 05
        #   11 15 16 06
        # B 10 09 08 07
        # B

        count = 1
        top, bottom = 0, n
        left, right = 0, n

        while left <= right:  # or top <= right
            # populate the top row
            for c in range(left, right):
                res[top][c] = count
                count += 1
            top += 1

            # populate the right column
            for r in range(top, bottom):
                res[r][right - 1] = count
                count += 1
            right -= 1

            # populate the bottom row (reverse order)
            for c in range(right - 1, left - 1, -1):
                res[bottom - 1][c] = count
                count += 1
            bottom -= 1

            # populate the left column (reverse order)
            for r in range(bottom - 1, top - 1, -1):
                res[r][left] = count
                count += 1
            left += 1
        """
        The time complexity is O(n^2) because each element is
        processed exactly once.

        The space complexity is O(1) as no data structures are used.
        """
        return res
