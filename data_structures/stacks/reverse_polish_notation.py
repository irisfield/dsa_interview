class Solution:
    """150. Evaluate Reverse Polish Notation"""
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:  # time O(n)
            if t == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))  # space O(n)
        return stack.pop()
