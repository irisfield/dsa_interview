class Solution:
    """84. Largest Rectangle in Histogram"""

    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)  # to handle edge case
        stack = [-1]  # to handle edge case
        area = 0

        for i, h in enumerate(heights):  # time O(n)
            print(f"{h} < {heights[stack[-1]]}")
            while h < heights[stack[-1]]:  # time O(2n)
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                area = max(area, height * width)
            stack.append(i)  # space O(n)
        """
        Time complexity is O(n), due to two iterations over heights and
        the stack.

        Space complexity is O(n), as the stack can hold all elements in
        the worst case.
        """
        return area

    def largestRectangleArea(self, heights: list[int]) -> int:
        area = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):  # time O(n)
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start = index
            stack.append((start, h))  # space O(n)

        for i, h in stack:  # time O(n)
            area = max(area, h * (len(heights) - i))
        """
        Time complexity is O(n), due to two iterations over heights and
        the stack.

        Space complexity is O(n), as the stack can hold all elements in
        the worst case.
        """
        return area
