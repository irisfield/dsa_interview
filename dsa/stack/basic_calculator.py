class Solution:
    """224. Basic Calculator"""

    def calculate(self, s: str) -> int:
        res, sign, stack = 0, 1, []

        cur = 0
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in "+-":
                res += cur * sign
                cur = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ")":
                res += cur * sign
                cur = 0
                res *= stack.pop()  # sign
                res += stack.pop()  # res

        """
        The time complexity is O(n), where n is the length of the input
        string. Each character is processed once.

        The space complexity is O(n), due to the stack used for storing
        results and signs during parentheses processing.
        """
        return res + (cur * sign)
