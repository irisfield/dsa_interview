class Solution:
    """121. Best Time to Buy and Sell Stock"""

    def maxProfit(self, prices: list[int]) -> int:
        low, maxProfit = float("inf"), 0
        for price in prices:
            low = min(low, price)
            if low < price:
                maxProfit = max(maxProfit, price - low)
        """
        Time complexity is O(n), as each element is processed once.
        Space complexity is O(1), as no data structures were utilized.
        """
        return maxProfit
