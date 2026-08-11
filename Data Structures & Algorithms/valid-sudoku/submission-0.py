class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols, rows, boards = defaultdict(set), defaultdict(set), defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                if (
                    val in cols[c] or
                    val in rows[r] or
                    val in boards[(r//3, c//3)]
                ):
                    return False

                cols[c].add(val)
                rows[r].add(val)
                boards[(r//3, c//3)].add(val)
        return True