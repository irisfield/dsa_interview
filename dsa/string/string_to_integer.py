class Solution:
    """8. String to Integer (atoi)"""

    def myAtoi(self, s: str) -> int:
        res, sign, read = 0, 1, False

        for c in s:  # O(n) time
            if c in " " and not read:
                continue
            elif c in "-+" and not read:
                read = True
                sign = 1 if c == "+" else -1
            elif c in "0123456789":
                read = True
                res = (res * 10) + int(c) if res > 0 else int(c)
            else:
                break

        maxInt = 2 ** 31 - 1
        if res > maxInt:
            res = maxInt if sign > 0 else maxInt + 1

        """
        The time complexity is O(n), as each character is processed
        exactly once.

        The space complexity is O(1), no data structures were utilized.
        """
        return res * sign
