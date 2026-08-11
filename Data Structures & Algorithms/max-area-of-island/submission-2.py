class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea, curarea = 0, 0
        m, n = len(grid), len(grid[0])
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            curarea = 0
            for dx, dy in direction:
                curarea += dfs(r+dx, c+dy)
            return curarea + 1

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    maxarea = max(maxarea, dfs(x, y))
        return maxarea