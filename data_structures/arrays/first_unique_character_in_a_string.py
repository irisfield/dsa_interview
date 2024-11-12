class Solution:
    """387. First Unique Character in a String"""

    def firstUniqChar(self, s: str) -> int:
        count = {}  # [count, index]

        for i, c in enumerate(s):  # O(n) time
            if c not in count:
                count[c] = [1, i]  # O(n) space
            else:
                count[c][0] += 1

        for c, i in count.values():  # O(n) time
            if c == 1:
                return i

        """
        The time complexity is O(n) as each letter is processed once.
        The space complexity is O(n) as a hash map is utilized.
        """
        return -1
