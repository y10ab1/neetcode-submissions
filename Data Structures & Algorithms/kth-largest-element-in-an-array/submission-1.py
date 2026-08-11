class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)

        while k > 0:
            k -= 1
            val = heapq.heappop(h)
        return -val