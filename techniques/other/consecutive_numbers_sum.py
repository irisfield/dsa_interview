class Solution:
    """829. Consecutive Numbers Sum"""

    def consecutiveNumbersSum(self, n: int) -> int:
        i, count = 1, 0
        while n > 0:
            n -= i
            if n % i == 0:
                count += 1
            i += 1

        """
        The time complexity is O(sqrt(n)) because the loop will
        run approximately sqrt(n) times.

        The space complexity is O(1) as no extra space is utilized.
        """
        return count
