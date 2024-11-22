class Solution:
    """74. Search a 2D Matrix"""

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Flatten the 2D matrix into a 1D array
        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            mid = l + (r - l) // 2

            # Convert mid to 2D matrix coordinates
            cell = matrix[mid // COLS][mid % COLS]

            if cell < target:
                l = mid + 1
            elif cell > target:
                r = mid - 1
            else:
                return True
        return False
        """
        The time complexity is O(log(m * n)). By virtually flattening
        the 2D matrix into a 1D array through clever conversion of the
        indexes, it becomes the same as searching a 1D array.

        The space complexity is O(1).
        """
