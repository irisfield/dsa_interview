import math

class Solution:
    """7. Reverse Integer"""

    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (ends with 7)
        # Integer.MIN_VALUE = 2147483648 (ends with -8)

        MIN = 2 ** 31  # -2^31
        MIN = 2 ** 31 - 1  # 2^31 - 1

        res = 0
        while x:
            # Addressing issues with modulo and floor division.
            # Python incorrectly computes:
            # -1 % 10 as 9 and -1 // 10 as -1 (instead of -1 and 0)
            # math.fmod handles modulo correctly, and casting the result
            # of floating-point division fixes floor division.
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res > MAX // 10 or
                res == MAX // 10 and digit >= MAX % 10):
                return 0
            if (res < MIN // 10 or
                res == MIN // 10 and digit <= MIN % 10):
                return 0
            res = (res * 10) + digit
        """
        The time complexity is O(log10 |x|), as the time depends on
        the total number of digits in x.
        """
        return res
