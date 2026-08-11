class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # just do dfs
        adj = defaultdict(list)
        visit = set()
        flag = True
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node, prev, flag):
            if node in visit:
                return False
            visit.add(node)
            for nxt in adj[node]:
                if nxt != prev:
                    flag &= dfs(nxt, node, flag)
            return flag

        flag &= dfs(0, -1, flag)
        return len(visit) == n and flag