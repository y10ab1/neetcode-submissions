class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dx, dy in direction:
                dfs(r+dx, c+dy)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    dfs(x, y)
                    cnt += 1
        return cnt