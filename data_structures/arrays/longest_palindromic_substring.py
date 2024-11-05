class Solution:
    """5. Longest Palindromic Substring"""

    def longestPalindrome(self, s: str) -> str:
        """
        What is the longest palindrome where s[i]
        is at the center of the string, expanding outward?
        """
        def palindrome(l, r, res):  # O(n) time
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r + 1]
                l, r = l - 1, r + 1
            return res

        res = ""
        for i in range(len(s)):  # O(n) time
            res = palindrome(i, i, res)  # odd length palindromes
            res = palindrome(i, i + 1, res)  # even length palindromes

        """
        The time complexity is O(n^2), as:
        - The loop runs O(n) times and calls an O(n) function twice.

        The space complexity is O(n), as res is O(n) in the worst case.
        """
        return res

    def longestPalindrome2(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            return s[0] if s[0] != s[1] else s

        res = ""
        for i in range(len(s)):  # O(n) time
            sub = s[i]
            for j in range(i + 1, len(s)):  # O(n) time
                sub += s[j]  # O(n) time
                if (sub == sub[::-1] and  # O(n) time
                    len(sub) > len(res)):
                    res = sub
        """
        The time complexity is O(n^3), as:
        - The outer loop runs O(n) times.
        - The inner loop runs O(n) times.
        - The substring concatenation and palindrome runs O(2n) time.

        The space complexity is O(n), as:
        - The space for sub, sub[::-1], and res is O(n) for each.
        - O(n) + O(n) + O(n) = O(n)
        """
        return res if res != "" else s[0]
