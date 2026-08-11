class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < minp:
                minp = prices[i]
            else:
                ans = max(prices[i]-minp, ans) 
        return ans