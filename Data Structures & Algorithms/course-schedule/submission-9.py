class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for dst, src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        q = deque([i for i in range(len(indegree)) if indegree[i] == 0])

        finish = 0
        while q:
            node = q.popleft()
            for dst in adj[node]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    q.append(dst)
            finish += 1

        return finish == numCourses