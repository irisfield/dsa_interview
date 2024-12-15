class Solution:
    """76. Minimum Window Substring"""

    def minWindow(self, s: str, t: str) -> str:
        """
        Sliding Window Approach:
        Use two pointers to dynamically expand and contract a window on string 's' to
        find the smallest substring that contains all characters from string 't'.
        """
        win = tuple()
        have, need = {}, {}
        count = 0

        for c in t:  # O(m) time
            have[c] = 0
            need[c] = need.get(c, 0) + 1

        l = 0
        # Find the first character in s that is needed
        while l < len(s) and s[l] not in need:  # O(n) time
            l += 1

        r = l
        while r < len(s):  # O(n) time
            if s[r] in need and have[s[r]] < need[s[r]]:
                count += 1
                have[s[r]] += 1
            elif s[r] in need:
                have[s[r]] += 1

            while count == len(t):
                curWin = r - l + 1
                prevWin = (win[1] - win[0] + 1) if win else float("inf")
                if curWin < prevWin:
                    win = (l, r)

                if s[l] in have:
                    have[s[l]] -= 1
                if s[l] in have and have[s[l]] < need[s[l]]:
                    count -= 1
                l += 1

            while l < len(s) and s[l] not in need:
                l += 1  # find the next character we need
            r += 1
        """
        The time complexity is O(n + m), where n and m are the lengths
        of the strings s and t. Both the left and right pointers
        traverse the string once, and the operations within the loop are
        constant.

        The space complexity is O(1). In the worst case, s and t can
        have up to k unique characters. But since both strings are
        guaranteed to consist of uppercase and lowercase English
        letters, k is a known constant: 26 + 26 = 52. Thus, k simplifies
        to O(1).
        """
        return s[win[0]:win[1] + 1] if win else ""
