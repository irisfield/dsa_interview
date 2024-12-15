class Solution:
    """48. Rotate Image"""

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #    L        R
        #  T 01 02 03
        #    08 09 04
        #    07 06 06
        #   B

        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # save the top left
                temp = matrix[top][left + i]

                #move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left into top right
                matrix[top + i][right] = temp  # top left

            right -= 1
            left += 1

        """
        The time complexity is O(n^2) as this is an n x n matrix.
        The space complexity is O(1) as no data structures were used.
        """
