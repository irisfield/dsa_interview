class Solution:
    """1849. Splitting a String Into Descending Consecutive Values"""

    def splitString(self, s: str) -> bool:
        def dfs(idx, prev):
            if idx == len(s):
                return True
            for j in range(idx, len(s))
                val = int(s[idx:j + 1])
                if (val + 1) == prev and dfs(j + 1, val):
                    return True
            return False

        for i in range(len(s) - 1):  # O(n) time
            # no restriction on what the first value can be
            val = int(s[:i + 1])
            if dfs(i + 1, val):  # O(n^2) time
                return True
        """
        The time complexity is O(n^3) due to the nested loops and
        recursion.

        The space complexity is O(n) due to the recursion stack.
        """
        return False
