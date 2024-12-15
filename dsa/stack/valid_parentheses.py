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
        """
        The time complexity is O(n), as each character in the string is
        processed once.

        The space complexity is O(n), as the stack can store up to
        n characters in the worst case.
        """
        return len(stack) == 0
