class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for r in range(m):
            dfs(r, 0)
            dfs(r, n-1)
        
        for c in range(n):
            dfs(0, c)
            dfs(m-1, c)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'