class Solution:
    """3. Longest Substring Without Repeating Characters"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        char = {}  # character : index
        for r in range(len(s)):
            if s[r] in char and char[s[r]] >= l:
                l = char[s[r]] + 1
            char[s[r]] = r
            res = max(res, r - l + 1)

        """
        The time complexity is O(n), as we process each character in the
        string once.

        The space complexity is O(min(n, m)), where n is the length of
        the string and m is the size of the character set.
        """
        return res
