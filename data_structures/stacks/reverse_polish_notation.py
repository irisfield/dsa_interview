class Solution:
    """150. Evaluate Reverse Polish Notation"""
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: b + a,
            "-": lambda a, b: b - a,
            "*": lambda a, b: b * a,
            "/": lambda a, b: int(b / a)
        }

        for t in tokens:  # time O(n)
            if t not in ops:
                stack.append(int(t))  # space O(n)
            else:
                res = ops[t](stack.pop(), stack.pop())
                stack.append(res)

        return stack.pop()
