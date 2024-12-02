# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    """278. First Bad Version"""

    def firstBadVersion(self, n: int) -> int:

        # if n is a bad version:
        #   check numbers smaller than n
        # if n is not a bad version:
        #   check numbers bigger than n

        l, r = 0, n

        while l <= r:
            v = l + ((r - l) // 2)

            if isBadVersion(v):
                r = v - 1
            else:
                l = v + 1
        """
        The time complexity is O(log n) as this is binary search.
        """
        return l + ((r - l) // 2) + 1
