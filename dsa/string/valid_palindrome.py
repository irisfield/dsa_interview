class Solution:
    """125. Valid Palindrome"""

    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())  # O(n) time and space
        """
        The time complexity is O(n), as each character is processed exactly once.
        The space complexity is O(n) for storing the filtered results.
        """
        return s == s[::-1]  # also O(n) time and space

    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r"[a-zA-Z0-9]", "", s).lower()  # O(n) time and space
        """
        The time complexity is O(n), as each character is processed exactly once.
        The space complexity is O(n) for storing the filtered results.
        """
        return s == s[::-1]  # also O(n) time and space
