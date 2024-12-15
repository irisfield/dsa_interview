class Solution:
    """74. Search a 2D Matrix"""

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = top + ((bot - top) // 2)

            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        if not (top <= bot):
            return False

        row = top + ((bot - top) // 2)
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True

        """
        The time complexity is O(log m + log n). Binary search is first
        applied to find the correct row, which takes O(log m) time, and
        then binary search is applied to the row to find the target,
        which takes O(log n) time

        The space complexity is O(1), as no data structures are used.
        """
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Flatten the 2D matrix into a 1D array
        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            # Convert mid to 2D matrix coordinates
            cell = matrix[mid // COLS][mid % COLS]

            if cell < target:
                l = mid + 1
            elif cell > target:
                r = mid - 1
            else:
                return True
        """
        The time complexity is O(log(m * n)). By virtually flattening
        the 2D matrix into a 1D array through clever conversion of the
        indexes, it becomes the same as searching a 1D array.

        The space complexity is O(1).
        """
        return False
