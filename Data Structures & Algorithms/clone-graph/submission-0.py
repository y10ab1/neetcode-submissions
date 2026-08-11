"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old2new = {node:Node(node.val)}
        queue = deque([node])
        while queue:
            old_node = queue.popleft()
            for n in old_node.neighbors:
                if n not in old2new:
                    old2new[n] = Node(n.val)
                    queue.append(n)
                old2new[old_node].neighbors.append(old2new[n])
        return old2new[node]