class Solution:
    """240. Search a 2D Matrix II"""

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        The goal is to remove a row or a column in each interation.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        r, c = 0, COLS - 1

        while r < ROWS and c >= 0:

            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else:
                return True
        """
        The time complexity is O(m + n) due to eliminating either a row
        or a column in each iteration.

        The space complexity is O(1) as no data structures are used.
        """
        return False
