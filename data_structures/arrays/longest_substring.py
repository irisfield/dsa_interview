class Solution:
    """3. Longest Substring Without Repeating Characters"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res, char = 0, 0, {}

        for r in range(len(s)):
            if s[r] in char and char[s[r]] >= l:
                l = char[s[r]] + 1
            char[s[r]] = r
            res = max(res, r - l + 1)
        """
        The time complexity is O(n), as each character is processed exactly once.
        The space complexity is O(1), as there are a constant number of letters.
        """
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        l, res = 0, 0

        while l < len(s):  # O(n) time
            chars = set()
            for i in range(l, len(s)):  # O(n) time
                if s[i] in chars:
                    break
                chars.add(s[i])  # O(1) space
            res = max(res, len(chars))
            l += 1

        """
        The time complexity is O(n^2) because for each character in the string,
        we may iterate through up to n characters in the inner loop.

        The space complexity is O(1), as there are a constant number of letters.
        """
        return res
