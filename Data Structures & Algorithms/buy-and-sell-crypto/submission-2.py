class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ptr_left=0
        ptr_right=1
        max_profit = 0

        while ptr_right < len(prices):
            if prices[ptr_right] > prices[ptr_left]:
                profit =   prices[ptr_right] - prices[ptr_left]
                max_profit = max(max_profit,profit)
            else:
                ptr_left = ptr_right
            ptr_right+=1        
        return max_profit