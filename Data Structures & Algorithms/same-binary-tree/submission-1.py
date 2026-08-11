# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # can have 0 node
        def dfs(n1, n2):
            if n1 and n2 and n1.val == n2.val:
                return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)
            elif n1 == None and n2 == None:
                return True
            else:
                return False
        return dfs(p, q)