class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 == s2:
                continue
            else:
                heapq.heappush(stones,s1-s2)
        
        if stones:
            return -1*stones[0]
        else:
            return 0