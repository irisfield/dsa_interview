class Solution:
    """57. Insert Interval"""

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):  # time O(n)
            iv = intervals[i]

            if (newInterval[1] < iv[0]):  # prepend interval
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > iv[1]:  # append interval
                res.append(iv)  # space O(n)
            else:  # merge interval
                newInterval = [min(newInterval[0], iv[0]), max(newInterval[1], iv[1])]

        res.append(newInterval)

        """
        Time complexity is O(n), as each element is processed once.
        Space complexity is O(n), as a list is used to store the result.
        """
        return res
