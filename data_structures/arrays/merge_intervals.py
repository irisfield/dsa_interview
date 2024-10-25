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
        return output

print(Solution().merge([[1,4],[0,2],[3,5]]))
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
