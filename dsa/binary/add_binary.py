class Solution:
    """67. Add Binary"""

    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        a, b = a[::-1], b[::-1]  # O(n) time

        for i in range(max(len(a), len(b))):  # O(n) time
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            res.append(str(total % 2))  # append either 0 or 1
            carry = total // 2

        if carry == 1:
            res.append("1")

        """
        The time complexity is O(n), where n is the length of the
        longest string. Each digit from both strings is processed once
        in the loop.

        The space complexity is O(n), where n is the length of the result string.
        """
        return "".join(reversed(res))

    return res
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
