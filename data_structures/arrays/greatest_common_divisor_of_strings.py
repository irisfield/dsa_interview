class Solution:
    """1071. Greatest Common Divisor of Strings"""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1

        res = ""
        for i in range(len(str2)):  # O(m) time
            sub = str2[:i + 1]
            p1 = len(str1) // len(sub)
            p2 = len(str2) // len(sub)

            # O(n + m) time
            if (sub * p1) == str1 and (sub * p2) == str2:
                if len(sub) > len(res):
                    res = sub

        """
        Let n = len(str1) and m = len(str2).

        The time complexity is O(m * (n + m)) because each comparison of
        sub * p1 and sub * p2 takes n + m time and this is done m times.

        The space complexity is O(m), as sub can be same length as str2.
        """
        return res

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1 // l, len2 // l
            return (str1[:l] * f1 == str1 and str1[:l] * f2 == str2)


        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        """
        The time complexity is O(min(m, n) * (m + n)) because the
        algorithm iterates through the shortest string the for
        the length of the strings combined.

        The space complexity is O(1) as no extra space is utilized.
        """
        return ""
