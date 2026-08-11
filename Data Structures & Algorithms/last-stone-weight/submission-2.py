class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-s for s in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            x = -heapq.heappop(neg_stones)
            y = -heapq.heappop(neg_stones)
            if x > y:
                heapq.heappush(neg_stones, y-x)
        
        if len(neg_stones) == 1:
            return -neg_stones[0]
        return 0