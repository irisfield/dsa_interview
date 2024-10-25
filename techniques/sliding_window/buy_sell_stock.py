class Solution:
    """121. Best Time to Buy and Sell Stock"""
    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            sell += 1
        """
        Time complexity is O(n), as each element is processed once.
        Space complexity is O(1), as no data structures were utilized.
        """
        return maxProfit

assert Solution().maxProfit([7,6,4,3,1]) == 0, "Expected 0"
assert Solution().maxProfit([7,1,5,3,6,4]) == 5, "Expected 5"
