class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        n = len(edges)
        indegree = defaultdict(int)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque([i for i in range(1, n+1) if indegree[i] == 1])

        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 1:
                    q.append(nxt)
        
        # now there are remaining cycle and seperated nodes
        for u, v in edges[::-1]:
            if indegree[u] > 0 and indegree[v] > 0:
                return [u, v]
        return []