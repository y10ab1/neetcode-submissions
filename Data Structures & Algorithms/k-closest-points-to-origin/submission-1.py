class Solution:
    def dis(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            h.append((self.dis(x,y,0,0),x,y))
        heapq.heapify(h)
        res = []
        while k>0:
            k -= 1
            _, x, y = heapq.heappop(h)
            res.append([x,y])
        return res