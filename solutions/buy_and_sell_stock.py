class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        l = 0 # buy
        r = 1 # selling

        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return maxProfit