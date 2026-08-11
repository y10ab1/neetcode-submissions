class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # use BFS start from each 0
        q = deque([])
        m, n = len(grid), len(grid[0])
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        visit = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
                    while q:
                        tx, ty = q.popleft()
                        dis = grid[tx][ty] + 1
                        # visit.add((tx, ty))
                        for dx, dy in direction:
                            if tx+dx >= 0 and ty+dy >= 0 and \
                            tx+dx < m and ty+dy < n and grid[tx+dx][ty+dy] > 0 \
                            and (tx+dx, ty+dy) not in visit:
                                grid[tx+dx][ty+dy] = min(grid[tx+dx][ty+dy], dis)
                                q.append([tx+dx, ty+dy])
                                visit.add((tx+dx, ty+dy))
                    visit = set()