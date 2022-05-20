class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1
        
        while r < len(prices):
            curr_max = 0
            if prices[r] - prices[l]  > 0:
                curr_max = prices[r] - prices[l]
            else: 
                l = r 
                
            max_profit = max(curr_max, max_profit)
            r += 1
            
        return max_profit
            
            
        
   