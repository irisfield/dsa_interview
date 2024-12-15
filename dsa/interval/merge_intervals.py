class Solution:
    """56. Merge Intervals"""

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: i[0])  # time O(n log n)
        output = [intervals[0]]

        for start, end in intervals[1:]:  # time O(n)
            prevEnd = output[-1][1]

            if start <= prevEnd:  # overlapping
                output[-1][1] = max(prevEnd, end)
            else:
                output.append([start, end])  # space O(n)

        """
        The time complexity is O(n log n). The algorithm sorts the
        intervals, which takes O(n log n), and then processes them in
        a single pass (O(n)).

        The space complexity is O(n). The space is used to store the
        output list, which may contain up to n intervals.
        """
        return output
