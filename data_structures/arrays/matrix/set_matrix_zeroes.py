class Solution:
    """73. Set Matrix Zeroes"""

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        first_row = False
        first_col = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Mark the columns to set to zeroes
                    if c > 0:
                        matrix[0][c] = 0
                    else:
                        first_col = True

                    # Mark the rows to set to zeroes
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        first_row = True

        # Set the rows/columns to zeroes
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    if matrix[r][c] != 0:
                        matrix[r][c] = 0

        # The set first column to zeroes
        if first_col:
            for r in range(ROWS):
                if matrix[r][0] != 0:
                    matrix[r][0] = 0

        # Set the first row to zeroes
        if first_row:
            for c in range(COLS):
                if matrix[0][c] != 0:
                    matrix[0][c] = 0
        """
        The time complexity is O(m * n). Each cell is visited up to
        two times.

        The space complexity is O(1) as no data structures were used.
        """


    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()

        for r in range(len(matrix)):  # O(m * n) time
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)  # O(m) space
                    cols.add(c)  # O(n) space

        for r in rows:  # O(m + n) time
            for c in range(len(matrix[r])):
                matrix[r][c] = 0

        for c in cols:  # O(m * n) time
            for r in range(len(matrix)):
                matrix[r][c] = 0
        """
        The time complexity is O(m * n). Each cell is visited up to
        three times.

        The space complexity is O(m + n). Sets are used to store up to
        m rows and n columns.
        """
