class Solution:
    """85. Maximal Rectangle"""

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # Convert the matrix to a histogram of heights, where each
        # element in the histogram represents the height of that column.
        # This is essentially transforming the problem into finding the
        # Largest Rectangle in a Histogram.
        ROWS, COLS = len(matrix), len(matrix[0])
        area = 0

        histogram = [0] * COLS  # O(n) space
        for r in range(ROWS):  # O(m * n) time
            for c in range(COLS):
                histogram[c] = histogram[c] + 1 if matrix[r][c] == "1" else 0
            print(histogram)
            area = max(area, self.largestRectangleArea(histogram))

        """
        The time complexity is O(m * n) as each element is processed once.
        The space complexity is O(n) due to the histogram and stack.
        """
        return area

    def largestRectangleArea(self, heights: list[int]) -> int:
        n, area = len(heights), 0

        stack = []  # (index, height)

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                area = max(area, h * (i - index))
                start = index
            stack.append((start, height))

        while stack:
            i, h = stack.pop()
            area = max(area, h * (n - i))

        """
        The time complexity is O(n) as each element is processed once.
        The space complexity is O(n) due to the stack.
        """
        return area
