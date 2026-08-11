class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, visit, prev_height):
            if i < 0 or j < 0 or i == m or j == n or prev_height > heights[i][j] \
            or (i, j) in visit:
                return
            visit.add((i, j))
            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])

        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n-1, atl, heights[r][n-1])

        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m-1, c, atl, heights[m-1][c])

        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in atl and (i, j) in pac:
                    res.append((i, j))
        return res