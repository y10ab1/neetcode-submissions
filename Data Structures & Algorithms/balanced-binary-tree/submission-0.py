# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.ans
    def dfs(self,node: Optional[TreeNode]):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if abs(left-right) > 1:
            self.ans = False
        return 1 + max(left, right)