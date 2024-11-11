class Solution:
    """1328. Break a Palindrome"""

    def breakPalindrome(self, palindrome: str) -> str:
        # find the first character that is not an a and make it an a
        p = list(palindrome)  # O(n) time and space

        if len(p) == 1:
            return ""

        swapped = None

        for i in range(len(p)):  # O(n) time
            if p[i] != "a":
                swapped = (i, p[i])
                p[i] = "a"
                break

        if p != p[::-1]:  # O(n) time
            return "".join(p)  # O(n) time

        if swapped:
            # undo the swap
            p[swapped[0]] = swapped[1]

        for i in range(len(p) - 1, -1, -1):  # O(n) time
            if p[i] == "a":
                p[i] = "b"
                break
        """
        The time complexity is O(n) as all operations scale linearly.
        The space complexity is O(n) as the string is converted to a list.
        """
        return "".join(p)
