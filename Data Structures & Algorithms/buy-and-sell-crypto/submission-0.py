class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_window_length=len(prices)
        max_profit=0
        for window_length in range(1,max_window_length):
            for i in range(0,len(prices)-window_length):
                profit=prices[i+window_length]-prices[i]
                if max_profit < profit:
                    max_profit = profit
        return max_profit