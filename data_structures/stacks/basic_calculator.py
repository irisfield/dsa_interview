class Solution:
    """224. Basic Calculator"""
    def calculate(self, s: str) -> int:
        res, sign, stack = 0, 1, []

        for c in s:
            if c.isdigit():
                res += int(c) * sign
            elif c in "+-":
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ")":
                res *= stack.pop()  # sign
                res += stack.pop()  # number
        return res

print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
print(Solution().calculate("2147483647"))  # 2147483647
