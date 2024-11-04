class Solution:
    """409. Longest Palindrome"""
    def longestPalindrome(self, s: str) -> int:
        count = {}
        res = 0
        for c in s:  # O(n) time
            count[c] = count.get(c, 0) + 1
            if count[c] % 2 == 0:
                res += 2
        """
        The time complexity is O(n), where n is the length of the string.
        The space complexity is O(1), as there are 52 unique characters.
        """
        return res if res == len(s) else res + 1

    def longestPalindrome(self, s: str) -> int:
        """
        For an odd length string, the longest palindrome is:
            - All pairs of characters that are the same
            - Plus a single character
        For an even length string, the longest palindrome is:
            - All pairs of characters that is the same
        """
        if len(s) == 1:
            return 1

        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        res = 0
        for v in count.values():
            if v & 1 == 0:  # even
                res += v
            elif v > 0:
                res += v - 1
        """
        The time complexity is O(n), where n is the length of the string.
        The space complexity is O(1), as there are 52 unique characters.
        """
        return res if res == len(s) else res + 1
