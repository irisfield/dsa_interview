class Solution:
    """20. Valid Parentheses"""
    def isValid(self, s: str) -> bool:
        pairs = { "(" : ")", "{" : "}", "[" : "]" }
        stack = []

        for p in s:  # time O(n)
            if p in pairs:
                stack.append(p)  # space O(n)
            elif len(stack) == 0 or pairs[stack.pop()] != p:
                    return False
        return len(stack) == 0

assert Solution().isValid("[") == False, "Expected False"
assert Solution().isValid("(]") == False, "Expected False"
assert Solution().isValid("([])") == True, "Expected True"
assert Solution().isValid("()[]{}") == True, "Expected True"
