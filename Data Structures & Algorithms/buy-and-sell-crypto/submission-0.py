class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[l]:
                l = i 

            profit = max(profit, prices[i] - prices[l])
        return profit






        