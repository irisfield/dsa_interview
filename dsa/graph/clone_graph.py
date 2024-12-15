"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """133. Clone Graph"""

    def cloneGraph(self, node: "Node") -> "Node":
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
    """
    The time complexity is O(V + E) because each node (V) and its edges (E) are traversed once.
    The space complexity is O(V) due to the dictionary storing clones and the maximum depth of the recursion stack.
    """
    return dfs(node) if node is not None else None
