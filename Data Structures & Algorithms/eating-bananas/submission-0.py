class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        left = 1
        right = max(piles)

        while left < right:
            k = left + (right - left) // 2    
            time_cost = 0
            for p in piles:
                time_cost+=math.ceil(p/k)
            if time_cost  > h:
                left = k+1
            else:
                right = k
        return left
