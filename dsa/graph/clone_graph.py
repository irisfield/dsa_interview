"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    """133. Clone Graph"""

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy = {}

        def dfs(node):
            if node in copy:
                return copy[node]

            clone = Node(node.val)
            copy[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        """
        The time complexity is O(n), where n is the number of nodes in
        the graph. Each node is visited exactly once during the DFS
        traversal, and each edge is processed once.

        The space complexity is O(n). This accounts for the space
        required by the recursion stack (which can grow up to the depth
        of the graph) and the hash map used to store the mapping of
        original nodes to their corresponding cloned nodes.
        """
        return dfs(node) if node is not None else None
