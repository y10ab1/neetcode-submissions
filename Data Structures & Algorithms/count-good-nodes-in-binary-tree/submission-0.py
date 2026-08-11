# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.cnt = 0

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, premax):
            if not node:
                return
            if node.val >= premax:
                self.cnt += 1
            premax = max(premax, node.val)
            dfs(node.left, premax)
            dfs(node.right, premax)
        
        dfs(root, root.val)
        return self.cnt