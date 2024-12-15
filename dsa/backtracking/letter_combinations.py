class Solution:
    """17. Letter Combinations of a Phone Number"""

    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        digitToChar = {
          "2": "abc",
          "3": "def",
          "4": "ghi",
          "5": "jkl",
          "6": "mno",
          "7": "qprs",
          "8": "tuv",
          "9": "wxyz",
        }

        def backtrack(i: int, curStr: str) -> None:
            if len(curStr) == len(digits):
                return res.append(curStr)
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        """
        The time and space complexity is O(n * 4 ^ n):
        - There are n characters in digits.
        - 7 and 9 are the worst case scenario mapping to 4 characters each.
        - There are 4 possible combinations for each of the 4 characters.
        """
        return res
