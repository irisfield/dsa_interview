class Solution:
    """242. Valid Anagram"""

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for c in s:  # O(n) time
            count[c] = count.get(c, 0) + 1

        for c in t:  # O(n) time
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        """
        The time complexity is O(n), where n is the length of the string.
        The space complexity is O(1), as there are 26 unique characters.
        """
        return True
