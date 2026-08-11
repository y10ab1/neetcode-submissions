class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.dfs(n-1, n, "(")
        return self.ans

    def dfs(self, l, r, stack):
        if l == 0 and r == 0:
            self.ans.append(stack)
            return

        if r > 0 and l < r:
            self.dfs(l, r-1, stack + ')')
        if l > 0:
            self.dfs(l-1, r, stack + '(')
            