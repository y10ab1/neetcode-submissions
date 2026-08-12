class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                taskcnt = -heapq.heappop(heap) # cnt of a task
                taskcnt -= 1
                if taskcnt:
                    q.append((taskcnt, time+n))
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(heap, -q.popleft()[0])
        
        return time


