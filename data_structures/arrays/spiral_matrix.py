class Solution:
    """54. Spiral Matrix"""

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []

        if not matrix:
            return res

        #   L   R
        # T 1 2 3
        #   8 9 4
        # B 7 6 5

        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while left < right and top < bottom:
            # every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # every i in the right most column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # every i in the left most column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        """
        The time complexity is O(m * n) because each element is
        processed exactly once.

        The space complexity is O(1) as no data structures are used.
        """
        return res
