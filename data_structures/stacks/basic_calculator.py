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
        return res + (cur * sign)

print(Solution().calculate("1-11"))  # -10
print(Solution().calculate("2147483647"))  # 2147483647
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
