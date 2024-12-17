class Solution:
    """67. Add Binary"""

    def addBinary(self, a: str, b: str) -> str:
        res = int(a, base=2) + int(b, base=2)
        """
        The time complexity is O(n + m), where n is the length of string
        a and m is the length of string b. This is because converting
        both strings to integers takes O(n) and O(m) time respectively,
        and the addition of integers takes O(max(n, m)) time. Converting
        the result back to binary also takes O(max(n, m)) time.

        The space complexity is O(max(n, m)), which is the space used
        for the binary strings a and b, as well as the result.
        """
        return bin(res)[2:]
