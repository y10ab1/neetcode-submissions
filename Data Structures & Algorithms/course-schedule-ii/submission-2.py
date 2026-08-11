class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for nxt, pre in prerequisites:
            adj[pre].append(nxt)
            indegree[nxt] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        ret = []

        while q:
            node = q.popleft()
            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
            ret.append(node)
            
        if len(ret) == numCourses:
            return ret
        return []