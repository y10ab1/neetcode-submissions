class Solution:
    def __init__(self):
        self.n_fresh = 0
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        m, n = len(grid), len(grid[0])
        visit = set()
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visit.add((i,j))
                elif grid[i][j] == 1:
                    self.n_fresh += 1
        
        if len(q) == 0 and self.n_fresh == 0:
            return 0

        def addcell(r,c):
            if r < 0 or c < 0 or r >=m or c >= n \
            or grid[r][c] != 1 or (r,c) in visit:
                return
            grid[r][c] = 2
            q.append((r,c))
            visit.add((r,c))
            self.n_fresh -= 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                visit.add((r,c))
                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)
            cnt += 1

        if self.n_fresh != 0:
            return -1
        return cnt - 1