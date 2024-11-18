class Solution:
    """387. First Unique Character in a String"""

    def firstUniqChar(self, s: str) -> int:
        count = {}

        for c in s:  # O(n) time
            count[c] = 1 + count.get(c, 0)  # O(1) space

        for i, c in enumerate(s):  # O(n) time
            if count[c] == 1:
                return i
        """
        The time complexity is O(n) as each element is processed once.
        The space complexity is O(1) since there are at most 26 unique
        lowercase letters in the input.
        """
        return -1
